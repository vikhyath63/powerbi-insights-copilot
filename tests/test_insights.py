from app.insights import build_insights
def test_filter_context_changes_results():
    result=build_insights(region="South")
    assert result["row_count"]==2 and result["total_revenue"]==4200
def test_no_match_is_explained():
    result=build_insights(region="Atlantis")
    assert result["row_count"]==0 and result["top_region"] is None
