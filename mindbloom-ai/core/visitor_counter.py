import os, uuid, requests
import streamlit as st

def _cfg():
    return (
        st.secrets.get("SUPABASE_URL", os.getenv("SUPABASE_URL", "")).rstrip("/"),
        st.secrets.get("SUPABASE_ANON_KEY", os.getenv("SUPABASE_ANON_KEY", "")),
    )

def register_visitor():
    if st.session_state.get("_visitor_registered"):
        return st.session_state.get("_visitor_count")
    url, key = _cfg()
    if not url or not key:
        return None
    try:
        r = requests.post(
            f"{url}/rest/v1/visitors",
            headers={"apikey": key, "Authorization": f"Bearer {key}",
                     "Content-Type": "application/json", "Prefer": "return=minimal"},
            json={"visitor_id": str(uuid.uuid4())}, timeout=5)
        r.raise_for_status()
        st.session_state["_visitor_registered"] = True
        count = get_visitor_count()
        st.session_state["_visitor_count"] = count
        return count
    except Exception:
        return None

def get_visitor_count():
    url, key = _cfg()
    if not url or not key:
        return None
    try:
        r = requests.get(
            f"{url}/rest/v1/visitors",
            headers={"apikey": key, "Authorization": f"Bearer {key}",
                     "Prefer": "count=exact", "Range": "0-0"},
            timeout=5)
        r.raise_for_status()
        cr = r.headers.get("Content-Range", "")
        if "/" in cr and cr.rsplit("/",1)[1] != "*":
            return int(cr.rsplit("/",1)[1])
        return None
    except Exception:
        return None

def render_visitor_gauge(count, maximum=1000):
    count = max(0, int(count or 0))
    maximum = max(100, int(maximum))
    pct = min(count / maximum, 1)
    angle = -90 + pct * 180
    st.markdown(f"""
<style>
.mb-vg{{max-width:430px;margin:22px 0;padding:18px 22px 14px;border:1px solid #dce9e0;border-radius:20px;background:#f7faf8;text-align:center}}
.mb-vt{{font:800 1.05rem "Trebuchet MS","Segoe UI",sans-serif;color:#234b39}}
.mb-vn{{font:900 2rem "Trebuchet MS","Segoe UI",sans-serif;color:#2f7655}}
.mb-dial{{position:relative;width:270px;height:140px;margin:8px auto 0;overflow:hidden}}
.mb-arc{{position:absolute;left:10px;top:10px;width:250px;height:250px;border-radius:50%;background:conic-gradient(from 270deg,#d7e7dc 0deg,#6da486 110deg,#2f7655 180deg,transparent 180deg)}}
.mb-arc:after{{content:"";position:absolute;left:18px;top:18px;width:214px;height:214px;border-radius:50%;background:#f7faf8}}
.mb-needle{{position:absolute;left:50%;bottom:5px;width:4px;height:105px;border-radius:4px;background:#234b39;transform-origin:50% 100%;transform:translateX(-50%) rotate({angle}deg);z-index:2}}
.mb-dot{{position:absolute;left:50%;bottom:0;width:14px;height:14px;transform:translateX(-50%);border-radius:50%;background:#234b39;z-index:3}}
.mb-scale{{display:flex;justify-content:space-between;margin:0 18px;color:#7b8981;font:700 .75rem "Segoe UI",sans-serif}}
.mb-note{{margin-top:7px;color:#7b8981;font:.78rem "Segoe UI",sans-serif}}
</style>
<div class="mb-vg">
<div class="mb-vt">👥 MindBloom Visitors</div>
<div class="mb-vn">{count:,}</div>
<div class="mb-dial"><div class="mb-arc"></div><div class="mb-needle"></div><div class="mb-dot"></div></div>
<div class="mb-scale"><span>0</span><span>{maximum:,}</span></div>
<div class="mb-note">Anonymous visits to MindBloom AI</div>
</div>
""", unsafe_allow_html=True)
