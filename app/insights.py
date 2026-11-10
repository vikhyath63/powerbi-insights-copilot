DATA=[{"region":"South","product":"Laptop","status":"Closed","revenue":1200},{"region":"North","product":"Phone","status":"Closed","revenue":800},{"region":"South","product":"Cloud","status":"Open","revenue":3000},{"region":"West","product":"Tablet","status":"Closed","revenue":500},{"region":"North","product":"Cloud","status":"Open","revenue":2500}]
def build_insights(region=None,product=None,status=None):
    rows=[r for r in DATA if (not region or r["region"].lower()==region.lower()) and (not product or r["product"].lower()==product.lower()) and (not status or r["status"].lower()==status.lower())]
    total=sum(r["revenue"] for r in rows); avg=total/len(rows) if rows else 0
    by_region={}
    for r in rows: by_region[r["region"]]=by_region.get(r["region"],0)+r["revenue"]
    leader=max(by_region,key=by_region.get) if by_region else None
    return {"filters":{"region":region,"product":product,"status":status},"row_count":len(rows),"total_revenue":round(total,2),"average_revenue":round(avg,2),"top_region":leader,"region_breakdown":by_region,"insight":f"{leader} leads revenue in the filtered data." if leader else "No rows match the selected filters.","rows":rows}
