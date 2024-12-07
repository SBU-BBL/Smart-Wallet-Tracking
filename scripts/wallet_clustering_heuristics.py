##########################################################################################################################################
##########################################################################################################################################
##############################################           Written by Noah Tover           #################################################
##########################################################################################################################################
##########################################################################################################################################
# This function assigns a unique number to all identifiers which show up together as the input of a transaction. The logic behind this heuristic is that keys are likely controlled all by one entity if they show up simultaneously, and that entity must own these wallets.
def commonSpendCluster(input_wallets, identifiers):
  # identifiers is expected to be a dataframe of the unique identifiers sorted. can easily be created with seq from 0 to max in identifiers too.
  ## TODO: Would be significantly faster to merge lists with any other lists with value in list for value in list. Then assign list objects a cluster. This way only searching through one column at a time.
  ## TODO: put identifiers.loc[identifiers['Identifier'].isin(senders), 'Cluster'] in a variable and use .update() method
  ## TODO: Write exceptions, define out complexity.
  ## TODO: Allow user to specify dependencies like column names.
  # Opportunity: Can use this skeleton to cluster change wallets and potentially create a more deep module. Just count number inputs an identifier is associated with, if one mark it as a change wallet.
  identifiers['Cluster'] = pd.NA
  cluster_count = 0
  for i in range(len(input_wallets)):
    senders = input_wallets.iloc[i].values[0]
    if all(sender.isna() for sender in senders):
      continue # Fix float doesnt work with this
    # Collapse already defined clusters into the first unique cluster they share if their identifiers are found to match in a row.
    if len(identifiers.loc[identifiers['Identifier'].isin(senders), 'Cluster']) == 0: # If an identifier is not associated with any outputs
      continue
    unique_clusters = identifiers.loc[identifiers['Identifier'].isin(senders), 'Cluster'].dropna().unique()
    # For each row of "From_Identifier", check if any of the identifiers within the list have non NA associated values in the column "Cluster".
    if len(unique_clusters) > 0:
      if len(unique_clusters) > 1:
        identifiers[identifiers['Cluster'].isin(unique_clusters.values)]['Cluster'] = unique_clusters[0].values
        identifiers.loc[identifiers['Identifier'].isin(senders), 'Cluster'] = unique_clusters[0]
        continue
      else:
        identifiers.loc[identifiers['Identifier'].isin(senders), 'Cluster'] = unique_clusters[0]
        continue
    else:
      # If no clusters exist for these identifiers, assign them a new unique cluster.
      identifiers.loc[identifiers['Identifier'].isin(senders), 'Cluster'] = cluster_count
      cluster_count += 1
  #TODO: Come up with a better name for identifiers
  # TODO: Sorting first might make things faster
  return identifiers

  ## TODO: Add change wallet clustering, behavior based, etc.
