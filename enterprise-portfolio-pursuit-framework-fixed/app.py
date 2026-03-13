import streamlit as st
import pandas as pd

st.set_page_config(page_title="Enterprise Pursuit Framework", layout="wide")

st.title("Enterprise Portfolio Pursuit Framework")
st.markdown("**Masonicare** — Executive Landscaping, Inc.  \nLast sync: just now")

if "data" not in st.session_state:
    st.session_state.data = {
        "strategic_fit": 8.9,
        "annual_value": 3_220_000,
        "snow_pct": 52,
        "new_haven_rev": 950_000,
        "fairfield_rev": 830_000,
        "hartford_rev": 820_000,
        "new_london_rev": 620_000,
    }

data = st.session_state.data


def enterprise_mix(revenue: int, annual_value: int) -> float:
    if annual_value <= 0:
        return 0.0
    return round((revenue / annual_value) * 100, 1)


tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    [
        "1. EOS Gate",
        "2. Financial Model",
        "3. Property Breakouts",
        "4. Competitive Displacement",
        "5. Operational Readiness",
        "6. EOS Tracker",
        "7. Export Report",
    ]
)

with tab1:
    st.header("SECTION 1 — Enterprise Qualification (EOS Gate)")
    col1, col2 = st.columns(2)

    with col1:
        data["strategic_fit"] = st.slider(
            "Strategic Fit Score",
            min_value=1.0,
            max_value=10.0,
            value=float(data["strategic_fit"]),
            step=0.1,
        )
        status_delta = "STRONG GO" if data["strategic_fit"] >= 8 else "REVIEW"
        st.metric("Overall Score", f"{data['strategic_fit']:.1f} / 10", status_delta)

    with col2:
        st.write("**Go / No-Go:** ✅ STRONG GO")
        st.write("**Target Win Date:** Q3 2026")
        st.write("**Executive Sponsor:** Masonicare Corporate Leadership")

with tab2:
    st.header("SECTION 2 — Enterprise Financial Model")
    st.metric("Modeled Annual Value", f"${data['annual_value']:,.0f}")
    st.write(f"**Revenue Mix** — Landscape {100 - data['snow_pct']}% | **Snow {data['snow_pct']}%**")

    branches = pd.DataFrame(
        {
            "Territory": ["New Haven", "Fairfield", "Hartford", "New London"],
            "Annual Revenue": [
                data["new_haven_rev"],
                data["fairfield_rev"],
                data["hartford_rev"],
                data["new_london_rev"],
            ],
            "% of Enterprise": [
                enterprise_mix(data["new_haven_rev"], data["annual_value"]),
                enterprise_mix(data["fairfield_rev"], data["annual_value"]),
                enterprise_mix(data["hartford_rev"], data["annual_value"]),
                enterprise_mix(data["new_london_rev"], data["annual_value"]),
            ],
            "Snow Exposure": [53, 54, 51, 52],
            "Complexity": [9.4, 8.7, 7.9, 7.2],
        }
    )
    st.dataframe(branches, use_container_width=True, hide_index=True)

with tab3:
    st.header("SECTION 3 — Property Breakouts")
    st.subheader("1. Wallingford Flagship (Priority #1)")
    st.write("**Financial:** Landscape $450k | Snow $500k | **Total $1.07M**")
    st.write("**Next Action:** Schedule site walk — March 15, 2026")

    with st.expander("Add future properties"):
        st.write("Use this area for Shelton Campus, Mystic, and future target sites.")

with tab4:
    st.header("SECTION 4 — Competitive Displacement Plan")
    incumbent = pd.DataFrame(
        {
            "Property": ["Wallingford Flagship", "Shelton Campus", "Mystic"],
            "Current Vendor": ["Regional Scaper", "Local Grounds Co", "Independent"],
            "Contract Expires": ["Jun 2027", "Nov 2026", "Mar 2027"],
            "Displacement Probability": ["78%", "65%", "82%"],
        }
    )
    st.dataframe(incumbent, use_container_width=True, hide_index=True)

with tab5:
    st.header("SECTION 5 — Operational Readiness Plan")
    st.write("**New Haven Branch (Pilot Ready)**")
    st.write("- Crews: 11 FT + 6 seasonal")
    st.write("- Salt storage: 240 tons secured")
    st.write("- 24/7 protocol documented")

with tab6:
    st.header("SECTION 6 — EOS Execution Tracker")
    st.write("**Q2 Rocks:**")
    st.write("✅ Secure executive introduction")
    st.write("✅ Wallingford site walk")
    st.metric("Pipeline Value", f"${data['annual_value']:,.0f}")

with tab7:
    st.header("Export Full Report")

    report = f"""# Masonicare Enterprise Pursuit Strategy

## Executive Summary
- Strategic Fit: {data['strategic_fit']:.1f}/10
- Annual Value: ${data['annual_value']:,.0f}
- Snow Mix: {data['snow_pct']}%

## Territory Revenue
- New Haven: ${data['new_haven_rev']:,.0f}
- Fairfield: ${data['fairfield_rev']:,.0f}
- Hartford: ${data['hartford_rev']:,.0f}
- New London: ${data['new_london_rev']:,.0f}

## Notes
Full 6-section report generated from the live dashboard.
"""

    st.download_button(
        label="Download Professional Markdown Report",
        data=report,
        file_name="Masonicare_Enterprise_Pursuit_Report.md",
        mime="text/markdown",
    )

    st.success("Markdown export is live. PDF export can be added next.")

with st.sidebar:
    st.header("Live Controls")
    data["annual_value"] = st.number_input(
        "Total Annual Value $",
        min_value=0,
        value=int(data["annual_value"]),
        step=10000,
    )
    data["snow_pct"] = st.slider(
        "Snow Revenue %",
        min_value=0,
        max_value=100,
        value=int(data["snow_pct"]),
        step=1,
    )
    st.button("Save to Session")
    st.info("All changes are live. Salesforce push button coming in v2.")

st.caption(
    "Enterprise Portfolio Pursuit Framework v1.0 • Ready for deployment • Built for Executive Landscaping, Inc."
)
