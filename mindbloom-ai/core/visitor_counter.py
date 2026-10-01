import os
import uuid
import requests
import streamlit as st


# =========================================================
# SUPABASE CONFIGURATION
# =========================================================

def _get_config():
    url = st.secrets.get(
        "SUPABASE_URL",
        os.getenv("SUPABASE_URL", "")
    ).rstrip("/")

    key = st.secrets.get(
        "SUPABASE_ANON_KEY",
        os.getenv("SUPABASE_ANON_KEY", "")
    )

    return url, key


# =========================================================
# GET TOTAL VISITOR COUNT
# =========================================================

def get_visitor_count():
    url, key = _get_config()

    if not url or not key:
        return None

    try:
        response = requests.get(
            f"{url}/rest/v1/visitors",
            headers={
                "apikey": key,
                "Authorization": f"Bearer {key}",
                "Prefer": "count=exact",
                "Range": "0-0",
            },
            timeout=5,
        )

        response.raise_for_status()

        content_range = response.headers.get(
            "Content-Range",
            ""
        )

        if "/" in content_range:
            total = content_range.rsplit("/", 1)[1]

            if total != "*":
                return int(total)

        return None

    except Exception:
        return None


# =========================================================
# REGISTER VISITOR
# =========================================================

def register_visitor():

    # Already registered during this Streamlit session
    if st.session_state.get("_visitor_registered"):

        # Return cached count if available
        cached_count = st.session_state.get(
            "_visitor_count"
        )

        if cached_count is not None:
            return cached_count

        # If count wasn't available earlier, try again
        count = get_visitor_count()

        st.session_state["_visitor_count"] = count

        return count


    url, key = _get_config()

    if not url or not key:
        return None


    try:
        visitor_id = str(uuid.uuid4())

        response = requests.post(
            f"{url}/rest/v1/visitors",
            headers={
                "apikey": key,
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "Prefer": "return=minimal",
            },
            json={
                "visitor_id": visitor_id
            },
            timeout=5,
        )

        response.raise_for_status()

        # Mark this Streamlit session as registered
        st.session_state["_visitor_registered"] = True

        # Get updated total
        count = get_visitor_count()

        st.session_state["_visitor_count"] = count

        return count

    except Exception:
        return None


# =========================================================
# VISITOR GAUGE
# =========================================================

def render_visitor_gauge(count, maximum=1000):

    if count is None:
        return

    count = max(0, int(count))

    maximum = max(
        100,
        int(maximum)
    )

    percentage = min(
        count / maximum,
        1
    )

    angle = -90 + (
        percentage * 180
    )


    st.markdown(
        f"""
        <style>

        /* =================================================
           VISITOR CARD
           ================================================= */

        .mb-visitor-card {{
            width: 100%;
            max-width: 430px;

            margin: 35px auto 20px auto;

            padding: 22px 20px 20px 20px;

            border: 1px solid #DCE9E0;

            border-radius: 20px;

            background: #F7FAF8;

            text-align: center;

            box-shadow:
                0 6px 18px rgba(35, 75, 57, 0.08);
        }}


        /* =================================================
           TITLE
           ================================================= */

        .mb-visitor-title {{
            font-family:
                "Trebuchet MS",
                "Segoe UI",
                Arial,
                sans-serif;

            font-size: 1.15rem;

            font-weight: 800;

            color: #234B39;

            margin-bottom: 3px;
        }}


        /* =================================================
           NUMBER
           ================================================= */

        .mb-visitor-number {{
            font-family:
                "Trebuchet MS",
                "Segoe UI",
                Arial,
                sans-serif;

            font-size: 2.4rem;

            font-weight: 900;

            color: #2F7655;

            line-height: 1.1;

            margin-top: 5px;
        }}


        /* =================================================
           GAUGE
           ================================================= */

        .mb-gauge {{
            position: relative;

            width: 280px;

            height: 150px;

            margin: 12px auto 0;

            overflow: hidden;
        }}


        /* =================================================
           GAUGE ARC
           ================================================= */

        .mb-gauge-arc {{
            position: absolute;

            left: 10px;

            top: 10px;

            width: 260px;

            height: 260px;

            border-radius: 50%;

            background:
                conic-gradient(
                    from 270deg,
                    #D7E7DC 0deg,
                    #6DA486 110deg,
                    #2F7655 180deg,
                    transparent 180deg
                );
        }}


        /* =================================================
           INNER GAUGE
           ================================================= */

        .mb-gauge-arc::after {{
            content: "";

            position: absolute;

            left: 18px;

            top: 18px;

            width: 224px;

            height: 224px;

            border-radius: 50%;

            background: #F7FAF8;
        }}


        /* =================================================
           NEEDLE
           ================================================= */

        .mb-gauge-needle {{
            position: absolute;

            left: 50%;

            bottom: 5px;

            width: 4px;

            height: 110px;

            border-radius: 4px;

            background: #234B39;

            transform-origin: 50% 100%;

            transform:
                translateX(-50%)
                rotate({angle}deg);

            z-index: 2;
        }}


        /* =================================================
           CENTER DOT
           ================================================= */

        .mb-gauge-dot {{
            position: absolute;

            left: 50%;

            bottom: 0;

            width: 15px;

            height: 15px;

            transform:
                translateX(-50%);

            border-radius: 50%;

            background: #234B39;

            z-index: 3;
        }}


        /* =================================================
           SCALE
           ================================================= */

        .mb-gauge-scale {{
            display: flex;

            justify-content: space-between;

            margin: 0 25px;

            color: #7B8981;

            font-family:
                "Segoe UI",
                Arial,
                sans-serif;

            font-size: 0.75rem;

            font-weight: 700;
        }}


        /* =================================================
           NOTE
           ================================================= */

        .mb-visitor-note {{
            margin-top: 8px;

            color: #7B8981;

            font-family:
                "Segoe UI",
                Arial,
                sans-serif;

            font-size: 0.78rem;
        }}

        </style>


        <div class="mb-visitor-card">

            <div class="mb-visitor-title">
                👥 MindHeal Visitors
            </div>

            <div class="mb-visitor-number">
                {count:,}
            </div>

            <div class="mb-gauge">

                <div class="mb-gauge-arc"></div>

                <div class="mb-gauge-needle"></div>

                <div class="mb-gauge-dot"></div>

            </div>

            <div class="mb-gauge-scale">

                <span>0</span>

                <span>{maximum:,}</span>

            </div>

            <div class="mb-visitor-note">
                Anonymous visits to MindHeal AI
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )
