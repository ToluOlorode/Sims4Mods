from drama_scheduler.drama_enums import DramaNodeScoringBucket

def add_buckets(drama):
    with DramaNodeScoringBucket.make_mutable():
        for dr, ama in drama.items():
            DramaNodeScoringBucket._add_new_enum_value(dr, ama)


BUCKET_ELEMENTS = {'Agency_Clients': 460337085}
add_buckets(BUCKET_ELEMENTS)
