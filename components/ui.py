import streamlit as st


def add_toast(message, type="success"):
    st.session_state.toasts.append({"msg": message, "type": type})
    st.rerun()


def render_toasts():
    toasts = st.session_state.get("toasts", [])
    if toasts:
        items = "".join(
            f'<div class="toast toast-{t["type"]}">{t["msg"]}</div>'
            for t in toasts[-3:]
        )
        st.html(f'<div class="toast-container">{items}</div>')
        st.session_state.toasts = []


def render_footer():
    st.html('<div class="footer">SocialPulse \u00a9 2026</div>')


def render_back():
    st.html(
        '<a href="?page=home" target="_self" class="back-btn">'
        '\u2190 Back</a>'
    )


def render_progress_bar():
    st.html('<div id="rdr-progress" class="progress-bar" style="width:0%;"></div>')