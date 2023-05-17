import dask.dataframe as dd

# write the time complexity of the function here


def process_csv(input_file, output_file):
    # Write the header to the output CSV file
    with open(output_file, 'w') as file:
        file.write("Song,Date,Number of Plays\n")

    # Read the input CSV file as a Dask dataframe
    df = dd.read_csv(input_file)

    # Group by 'Song' and 'Date' columns and sum the 'Number of Plays' column
    aggregated_df = df.groupby(['Song', 'Date'])[
        'Number of Plays'].sum().reset_index()

    # Write the aggregated data to the output CSV file
    aggregated_df.to_csv(output_file, index=False,
                         header=False, mode='a', single_file=True)

    return output_file
