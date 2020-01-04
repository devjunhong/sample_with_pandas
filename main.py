import pandas as pd


def print_data_frame_with_desc(desc, df):
    print('********* [ %s ] *********' % desc)
    print(df.head())
    print(len(df))


def main():
    # Step 2. Load dataset 
    file_name = "https://raw.githubusercontent.com/" \
                "uiuc-cse/data-fa14/gh-pages/data/iris.csv"
    df = pd.read_csv(file_name)
    print_data_frame_with_desc('the original source', df)

    # Step 3. Sort by column in pandas data frame
    df = df.sort_values(by=['sepal_length'])
    print_data_frame_with_desc('sort in sepal_length', df)

    # Step 4. Select top to 30th row
    df = df.iloc[0:30]
    print_data_frame_with_desc('select from top to 30th', df)

    # Step 5. Random sampling
    sampled_df = df.sample(5)
    print_data_frame_with_desc('select from top to 30th', sampled_df)


if __name__ == '__main__':
    main()
