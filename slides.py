import streamlit as st
import reveal_slides as rs

with open("slide.md", "r", encoding="utf-8") as f:
    slides_content = f.read()

rs.slides(
    content=slides_content,
    theme="moon",
    height=600,
    config={
        "controls": True,
        "progress": True,
        "center": True,
        "transition": "slide",
        "plugins": ["highlight"],
        "pluginsConfig": {
            "highlight": {
                "theme": "vs"
    }
        }
    }
)
st.markdown(
    """
    <style>
.reveal pre code {
    font-size: 1.25em;            
    line-height: 1.5;             
    background-color: #fafafa;    
    padding: 16px 20px;           
    border-radius: 12px;           
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); 
    color: #333333;                
    font-family: 'Fira Code', Consolas, 'Courier New', monospace; 
    white-space: pre-wrap;        
    transition: background-color 0.3s ease;
}

.reveal pre code:hover {
    background-color: #f0f0f0;    
}
</style>

    """,
    unsafe_allow_html=True
)