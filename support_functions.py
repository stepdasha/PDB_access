import biotite.database.rcsb as rcsb
import datetime

def get_spike_ids(uniprot_id = "P0DTC2" , min_weight = 400, max_resolution = 4.0):
    """
    get all pdbs with defined weight and resolution, 
    input the uniprot_id (the default is spike), min_weight , and max_resolution
    """
    #uniprot_id = "P0DTC2" #spike in Sars-cov-2
    #max_resolution = 4.0
    #min_weight =400 
    """
    in Da, structure min mass to get rid of rbd only structures,
    Spike mass is 429 Da.
    """
    query_by_uniprot_id = rcsb.FieldQuery(
        "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession",
        exact_match=uniprot_id,
    )
    today = datetime.datetime.now()
    print(
        f"Number of structures on {today.year}-{today.month}-{today.day}: {rcsb.count(query_by_uniprot_id)}"
    )

  
    query_by_resolution = rcsb.FieldQuery(
        "rcsb_entry_info.resolution_combined", less_or_equal=max_resolution
    )
    print(
        f"Number of structures with resolution less than or equal to {max_resolution}: {rcsb.count(query_by_resolution)}"
    )


    query_by_polymer_weight = rcsb.FieldQuery(
        "rcsb_entry_info.molecular_weight", greater=min_weight
    )
    print(
        f"Number of structures with mass more than or equal to {min_weight}: {rcsb.count(query_by_polymer_weight)}"
    )


    query = rcsb.CompositeQuery(
        [
            query_by_uniprot_id,
            query_by_resolution,
            #query_by_polymer_count,
            query_by_polymer_weight, 
        ],
        "and",
    )
    pdb_ids = rcsb.search(query)
    print(f"Number of spike matches: {len(pdb_ids)}")
    print("Selected PDB IDs:")
    print(*pdb_ids)
    return(pdb_ids)


    