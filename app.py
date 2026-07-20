import streamlit as st

from data.data_utils import get_sp500_tickers
from tabs import tab_summary, tab_chart, tab_statistics, tab_portfolio, tab_montecarlo, tab_chatbot


st.set_page_config(page_title="FinDash", layout="wide")


def main():
    st.sidebar.title("FinDash")

    ticker_list = ["-"] + get_sp500_tickers()
    ticker = st.sidebar.selectbox("Select a ticker", ticker_list)

    select_tab = st.sidebar.radio(
        "Select tab",
        [
            "Summary",
            "Chart",
            "Statistics",
            "Financials",
            "Analysis",
            "Portfolio Analysis (CAPM/APT)",
            "Monte Carlo Simulation",
            "Chatbot",
        ],
    )

    if select_tab == "Summary":
        tab_summary.render(ticker)
    elif select_tab == "Chart":
        tab_chart.render(ticker)
    elif select_tab == "Statistics":
        tab_statistics.render_statistics(ticker)
    elif select_tab == "Financials":
        tab_statistics.render_financials(ticker)
    elif select_tab == "Analysis":
        tab_statistics.render_analysis(ticker)
    elif select_tab == "Portfolio Analysis (CAPM/APT)":
        tab_portfolio.render()
    elif select_tab == "Monte Carlo Simulation":
        tab_montecarlo.render(ticker)
    elif select_tab == "Chatbot":
        tab_chatbot.render(ticker)


if __name__ == "__main__":
    main()
