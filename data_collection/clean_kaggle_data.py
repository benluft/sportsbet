import pandas as pd
import os

DATA_DIR = os.path.join(os.getcwd(), r'../data/')


def _get_dataframe():
    csv_path = os.path.join(DATA_DIR, r'spreadspoke_scores.csv')
    df_full = pd.read_csv(csv_path)
    df_full = df_full.drop(columns=['weather_detail', 'stadium'])
    df_full = df_full.dropna(subset=['score_home', 'score_away'])
    print(df_full.tail().to_string())
    print(df_full.columns)
    print(df_full.head())
    return df_full


def _map_team_name_to_abbrev(df_original):
    csv_path = os.path.join(DATA_DIR, r'nfl_teams.csv')
    team_df = pd.read_csv(csv_path)
    team_df = team_df[['team_name', 'team_id']]
    team_df = team_df.set_index('team_name')
    team_dict = team_df.to_dict('index')
    team_dict = {key: value['team_id'] for key, value in team_dict.items()}
    df_original['team_home'] = df_original['team_home'].map(team_dict)
    df_original['team_away'] = df_original['team_away'].map(team_dict)
    return df_original


def get_kaggle_data():
    df_out = _get_dataframe()
    df_out = _map_team_name_to_abbrev(df_out)
    return df_out


if __name__ == '__main__':
    df = _get_dataframe()
    df = _map_team_name_to_abbrev(df)
    print(df.to_string())
