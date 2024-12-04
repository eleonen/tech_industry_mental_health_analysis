from typing import List, Tuple, Dict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

colors = ["#ca0020", "#92c5de"]

text_to_num_mapping = {
    "Yes": 1,
    "Yes, all of them": 1,
    "No": 0,
    "None of them": 0,
    "Some did": 0.5,
    "Some of them": 0.5,
    "Maybe": 0.5,
    None: None,
}


def find_outliers(df: pd.DataFrame, features: List[str]) -> List[int]:
    """
    Detects unique outliers in multiple features using the IQR method.

    Args:
        df: DataFrame containing the data.
        features: List of features to detect outliers in.

    Returns:
        List containing the outliers.
    """
    outliers_list = []
    for feature in features:
        if feature not in df.columns:
            print(f"Feature '{feature}' not found in DataFrame.")
            continue

        q1 = df[feature].quantile(0.25)
        q3 = df[feature].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        feature_outliers = df[
            (df[feature] < lower_bound) | (df[feature] > upper_bound)
        ][feature]
        feature_outliers_unique = [int(value) for value in
                                   feature_outliers.unique()]

        for value in feature_outliers_unique:
            if value not in outliers_list:
                outliers_list.append(value)

        if feature_outliers_unique:
            print(f"Unique outliers in '{feature}': {feature_outliers_unique}")
        else:
            print(f"No outliers in '{feature}'")

    return outliers_list


def create_age_histplot(df: pd.DataFrame) -> None:
    """
    Creates histograms of respondents' ages (18-64) for each survey year.

    Args:
        df: DataFrame containing survey data with columns 'QuestionID',
            'AnswerText', and 'SurveyID'.

    Returns:
        None
    """
    age_df = df[
        (df["QuestionID"] == 1)
        & (pd.to_numeric(df["AnswerText"], errors="coerce").between(18, 64))
    ]
    survey_years = age_df["SurveyID"].unique()

    fig, axes = plt.subplots(1, 5, figsize=(15, 5), sharey=True)
    axes = axes.flatten()

    for i, year in enumerate(survey_years):
        ax = axes[i]
        data = age_df[age_df["SurveyID"] == year]["AnswerText"].astype(int)
        sns.histplot(data, ax=ax, bins=10, kde=True)
        ax.set_title(f"Year: {year}")
        ax.set_xlabel("")
        ax.set_ylabel("Number of Respondents")

    fig.supxlabel("Age")
    fig.suptitle("Distribution of Respondents by Working Age (18-64), by Survey Year")
    plt.show()


def create_gender_barplot(df: pd.DataFrame) -> None:
    """
    Creates a bar plot showing gender distribution for each survey year.

    Args:
        df: DataFrame containing survey data with columns 'QuestionID',
            'AnswerText', and 'SurveyID'.

    Returns:
        None
    """
    gender_df = df[df["QuestionID"] == 2]
    gender_counts = (
        gender_df.groupby(["SurveyID", "AnswerText"])
        .size()
        .reset_index(name="Count")
        .sort_values(by=["SurveyID", "AnswerText"])
    )
    gender_sum = gender_counts.groupby("SurveyID")["Count"].transform("sum")
    gender_counts["Percentage"] = gender_counts["Count"] / gender_sum * 100

    ax = sns.barplot(
        data=gender_counts, x="SurveyID", y="Count", hue="AnswerText", dodge=True
    )

    n_categories = len(gender_counts["AnswerText"].unique())
    width = 0.8
    category_width = width / n_categories

    for i, year in enumerate(gender_counts["SurveyID"].unique()):
        for j, gender in enumerate(gender_counts["AnswerText"].unique()):
            data = gender_counts[
                (gender_counts["SurveyID"] == year)
                & (gender_counts["AnswerText"] == gender)
            ]
            if not data.empty:
                x = i + (j - 1) * category_width
                plt.text(
                    x,
                    data["Count"].iloc[0],
                    f"{data['Percentage'].iloc[0]:.1f}%",
                    ha="center",
                    va="bottom",
                )
    ax.legend(title="Answers")
    plt.title("Number of Respondents by Gender, by Survey Year")
    plt.xlabel("Survey Year")
    plt.ylabel("Number of Respondents")
    plt.tight_layout()
    plt.show()


def create_lineplot(df: pd.DataFrame, questions: List[int], text: str) -> None:
    """
    Creates line plots showing percentages of responses for two survey questions over time.

    Args:
        df: DataFrame containing survey data with columns 'QuestionID',
            'AnswerText', and 'SurveyID'.
        questions: List of two QuestionIDs for plotting.
        text: Text describing the questions.

    Returns:
        None
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=True)
    axes = axes.flatten()

    for ax, question_id in zip(axes, questions):
        curr_df = df[(df["QuestionID"] == question_id)].copy()
        df_counts = (
            curr_df.groupby(["SurveyID", "AnswerText"]).size().reset_index(name="Count")
        )
        df_pivoted = df_counts.pivot_table(
            index="SurveyID", columns="AnswerText", values="Count", aggfunc="sum"
        )
        df_pivoted_pct = df_pivoted.div(df_pivoted.sum(axis=1), axis=0) * 100
        sns.lineplot(data=df_pivoted_pct, ax=ax)
        ax.set_xlabel("")
        ax.set_xticks(df_pivoted_pct.index)
        if question_id == questions[0]:
            ax.set_title("$\mathbf{{Current}}$ employer " + text)
        else:
            ax.set_title("$\mathbf{{Previous}}$ employer " + text)
        ax.legend(loc="upper left", title="Answers")

    axes[0].set_ylabel("Percentage of Respondents")
    fig.supxlabel("Survey Year")
    plt.show()


def create_prevalence_barplot(df: pd.DataFrame, q1: int, q2: int) -> None:
    """
    Creates a bar plot showing the prevalence rates of the top 3 mental health issues in 2016.

    Args:
        df: DataFrame containing survey data with columns 'QuestionID',
            'AnswerText', and 'SurveyID'.
        q1: QuestionID for calculating the total number of respondents.
        q2: QuestionID for determining the top 3 mental health issues.

    Returns:
        None
    """
    respondents = df[(df["QuestionID"] == q1) & (df["SurveyID"] == 2016)][
        "AnswerText"
    ].count()

    top_3_diagnoses = (
        df[df["QuestionID"] == q2]["AnswerText"].value_counts().head(3).reset_index()
    )
    top_3_diagnoses["PrevalenceRate"] = top_3_diagnoses["count"] / respondents
    top_3_diagnoses["Percentage"] = top_3_diagnoses["PrevalenceRate"] * 100
    top_3_diagnoses["CI%"] = (
        1.6456
        * (
            np.sqrt(
                top_3_diagnoses["PrevalenceRate"]
                * (1 - top_3_diagnoses["PrevalenceRate"])
                / respondents
            )
        )
        * 100
    )

    sns.barplot(data=top_3_diagnoses, y="AnswerText", x="Percentage")
    plt.errorbar(
        x=top_3_diagnoses["Percentage"],
        y=top_3_diagnoses["AnswerText"],
        xerr=top_3_diagnoses["CI%"],
        c="#0571b0",
        fmt="none",
        capsize=5,
    )
    plt.ylabel("Mental health issue")
    plt.title(
        "Prevalence rate of the 3 most common Mental Health issues in "
        "$\mathbf{2016}$ (with confidence level of $\mathbf{90\%}$)"
    )
    plt.show()


def create_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Creates a heatmap of correlations between survey responses for specific questions.

    Args:
        df: DataFrame containing survey data with mappable values.

    Returns:
        None
    """
    df = df.copy()
    for col in df.columns:
        df[col] = df[col].map(text_to_num_mapping).convert_dtypes().fillna(df[col])
    df = df.apply(pd.to_numeric, errors="coerce")
    correlation = df.corr()
    mask = np.triu(np.ones_like(correlation, dtype=bool))
    sns.heatmap(data=correlation, mask=mask, vmax=1, vmin=-1, cmap="vlag", annot=True)
    plt.title("Correlation Heatmap of Physical/Mental Health importance questions")
    plt.show()


def create_violin_subplots(
    question_pairs: List[Tuple[int, int]],
    question_labels: Dict[int, str],
    df: pd.DataFrame,
    title: str,
) -> None:
    """
    Creates violin plots comparing responses for pairs of questions.

    Args:
        question_pairs: List of tuples with QuestionIDs to compare.
        question_labels: Mapping of QuestionIDs to descriptive labels.
        df: DataFrame containing survey data with columns 'UserID',
            'QuestionID', and 'AnswerText'.
        title: Title for the plot.

    Returns:
        None
    """
    fig, axes = plt.subplots(
        len(question_pairs), 1, figsize=(9, 4 * len(question_pairs))
    )
    if len(question_pairs) == 1:
        axes = [axes]
    for i, (q1, q2) in enumerate(question_pairs):
        temp_df = df.reset_index().melt(
            id_vars="UserID",
            value_vars=[q1, q2],
            var_name="QuestionID",
            value_name="AnswerText",
        )

        temp_df["Label"] = temp_df["QuestionID"].map(question_labels)
        if temp_df["AnswerText"].str.isnumeric().all():
            temp_df["AnswerText"] = pd.to_numeric(
                temp_df["AnswerText"], errors="coerce"
            )
            y_column = "AnswerText"
        else:
            temp_df["AnswerNumeric"] = temp_df["AnswerText"].map(text_to_num_mapping)
            y_column = "AnswerNumeric"

        sns.violinplot(
            data=temp_df,
            ax=axes[i],
            x="Label",
            y=y_column,
            split=True,
            inner=None,
            palette=colors,
            hue="Label",
            legend=False,
        )

        if y_column == "AnswerNumeric":
            axes[i].set_yticks([0, 0.5, 1])
            axes[i].set_yticklabels(["No", "Some", "Yes"])

        axes[i].set_xlabel("")
        axes[i].set_ylabel("Answers")

    fig.suptitle(f"{title}")
    plt.tight_layout()
    plt.show()
