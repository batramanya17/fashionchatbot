import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="The Everyday Style Edit",
    page_icon="👗",
    layout="centered",
)

MANUAL = r"""
# Knowledge Summary: The Everyday Style Edit

Based on the uploaded Fashion Styling Guide PDF

## 1. Overview
The Everyday Style Edit is a practical fashion and styling guide designed to help students choose comfortable, fashionable and well-coordinated outfits for different situations.

It focuses on:
- Day-wise outfit planning.
- College and university outfits.
- Rainy-day dressing.
- Low-energy or bad-day outfits.
- Colour combinations and outfit coordination.
- Styling techniques, accessories, footwear and bags.
- Building confidence through comfortable dressing.

Main philosophy: Style should feel like you. Fashion should be simple, practical and comfortable rather than complicated.

## 2. Basic fashion styling principles
The guide follows a simple three-step outfit formula:
1. Base: Choose jeans, trousers, skirts or a kurta.
2. Top: Select a fitted, relaxed or layered top depending on the bottom.
3. Finish: Add clean shoes, a bag and one accessory.

### Essential wardrobe pieces
- Dark-blue wide-leg jeans.
- Black or beige trousers.
- White, cream and black tops.
- Brown or chocolate tops.
- Relaxed shirts.
- Kurta sets.
- Lightweight cardigans and overshirts.
- Comfortable sneakers and flat sandals.
- Neutral everyday bags.

### Easy colour combinations
| Combination | Style |
|---|---|
| Brown + Cream | Elegant |
| Blue Denim + White | Classic |
| Sage + Beige | Soft and minimal |
| Black + Light Blue | Smart casual |
| Chocolate + Denim | Trendy |
| Soft Pink + Grey | Feminine and subtle |

## 3. Day-wise outfit planning
| Day | Outfit recommendation |
|---|---|
| Monday | Dark-blue wide-leg jeans + cream/white top + sneakers |
| Tuesday | Straight trousers + relaxed tee or striped shirt |
| Wednesday | Black/beige trousers + brown or pastel top |
| Thursday | Wide-leg jeans + fitted tee + open shirt |
| Friday | Dark denim + dressier top + clean flats |
| Saturday | Comfortable jeans/joggers + breathable tee |
| Sunday | Kurta set, relaxed co-ord or comfortable trousers |

The purpose is to create variety without purchasing new clothes every day.

## 4. College-day styling
College outfits should balance comfort, practicality and appearance.

Four important outfit categories:
- Classic campus: Wide-leg denim, plain top, sneakers and backpack.
- Presentation/Viva: Tailored trousers, tucked-in shirt, loafers or flats and watch.
- Long college day: Comfortable jeans, breathable tee, overshirt and cushioned sneakers.
- Events/Fests/Project Expo: Coordinated top and trousers, kurta set or dark jeans with a dressier top.

### College styling rules
- Check the timetable and weather beforehand.
- Wear shoes suitable for walking.
- Keep your bag organised.
- Carry a lightweight layer.
- Choose clothes that allow comfortable movement.

## 5. Rainy-day fashion
Rainy-day dressing should prioritise quick-drying fabrics, easy-to-clean clothing and footwear with good grip.

### Three recommended looks
1. Cropped trousers + cotton tee + waterproof jacket + water-resistant sneakers.
2. Dark jeans + tucked tee + rain jacket + secure sandals.
3. Simple kurta + ankle-length pants + quick-dry layer + practical flats.

What to wear:
- Darker bottoms.
- Shorter hems.
- Breathable tops.
- Lightweight layers.
- Quick-drying fabrics.
- Secure footwear.

What to avoid:
- Floor-length wide trousers.
- Delicate suede.
- Slippery footwear.
- Very long palazzos.
- Heavy fabrics that remain wet.

### Rainy-day essentials
Compact umbrella, tissues, waterproof phone pouch, spare hair tie and bag cover.

## 6. Outfits for bad or low-energy days
The guide recognises that some days you may feel tired, bloated, rushed or simply not interested in dressing up.

Three outfit formulas are suggested:
- No-thinking outfit: Comfortable jeans + plain tee + sneakers + everyday bag.
- Comfort-first outfit: Relaxed trousers + oversized shirt + comfortable flats.
- Quick polished outfit: Black/beige trousers + brown/cream top + watch + neat hair.

### Five-minute styling reset
1. Pick comfortable, clean clothes.
2. Choose one colour family.
3. Brush or tie your hair.
4. Add one accessory.
5. Take your bag and go.

The key message is that comfort is also a fashion choice.

## 7. Important styling techniques
| Technique | Purpose |
|---|---|
| Full tuck | Creates a sharper appearance |
| Front tuck | Adds relaxed waist definition |
| No tuck | Creates an oversized look |
| Open shirt layering | Adds dimension to simple outfits |
| Accessories | Adds a finishing touch |
| Clean sneakers | Makes casual outfits look polished |
| Loafers/flats | Makes trousers look smarter |

### Bag styling
- Backpack: Best for busy college days.
- Structured tote: Best for presentations and shorter days.

### Hairstyle ideas
- Claw clip.
- Low ponytail.
- Braid.
- Open hair.

## 8. Outfit problem-solving
| Problem | Solution |
|---|---|
| Outfit looks oversized | Add a front tuck or structured bottom |
| Outfit looks too plain | Add a belt, watch or open shirt |
| Outfit looks too dressy | Switch to sneakers |
| Weather changes | Carry a lightweight layer |

## 9. Weekly outfit preparation
The guide recommends planning outfits the night before to reduce morning stress.
- Monday: Dark denim + light top.
- Tuesday: Trousers + relaxed shirt.
- Wednesday: Tailored bottom + brown/pastel top.
- Thursday: Denim + tee + overshirt.
- Friday: Dressier top + denim/trousers.
- Saturday: Relaxed casual set.
- Sunday: Kurta/co-ord/comfort look.

## 10. Core knowledge for a Fashion Stylist Chatbot
The chatbot should support outfit recommendations, day-wise styling, college fashion, weather-based styling, mood-based outfits, colour coordination, body-proportion and fit suggestions, accessories, outfit troubleshooting and wardrobe planning.

## Final knowledge statement
The Everyday Style Edit teaches that good fashion is not about owning expensive clothes or following every trend. It is about understanding outfit combinations, choosing suitable colours, balancing proportions, dressing according to weather and occasion, and feeling confident in what you wear.

The chatbot's main objective is to act as a personal everyday fashion stylist that recommends what to wear, how to style it, what to avoid and how to make existing wardrobe pieces look fashionable.
"""

SYSTEM_PROMPT = """
You are The Everyday Style Edit, a friendly, knowledgeable and practical personal fashion stylist.

Use the supplied fashion manual as your primary knowledge source. Answer questions using its guidance. If a topic is not covered, say so briefly and then clearly label any additional advice as general styling guidance. Do not pretend that unsupported details came from the manual.

Help with:
- College, presentation, event and everyday outfits.
- Day-wise outfit planning.
- Rainy-day and practical weather-aware dressing.
- Low-energy or comfort-first outfits.
- Colour coordination, footwear, bags, accessories and hairstyles.
- Styling clothes the user already owns.
- Simple fit and proportion suggestions without body-shaming.

When recommending a complete outfit, organise it naturally using:
**Top, Bottom, Footwear, Bag, Accessories, Hairstyle, How to style it, and Why it works.**
Only include sections that are relevant; do not force this format for every question.

Be friendly, supportive, concise and practical. Use simple English. Ask one focused follow-up question only when essential information is missing. Never judge the user's body, budget or fashion choices. Do not claim to know current weather unless the user provides it.
"""

st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(180deg, #fbf7f1 0%, #fffdfa 42%, #f8f4ee 100%); }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .hero {
        padding: 1.6rem 1.5rem; border-radius: 22px;
        background: linear-gradient(120deg, #eee2d3, #f8eee6 55%, #e7e3d9);
        border: 1px solid #e5d8ca; margin-bottom: 1.2rem;
    }
    .hero h1 { color: #4b382d; font-family: Georgia, serif; margin: 0; }
    .hero p { color: #725c4e; margin: .45rem 0 0 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
      <h1>THE EVERYDAY STYLE EDIT</h1>
      <p>Your personal everyday fashion stylist · Dress effortlessly. Style confidently.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.subheader("Your styling assistant")
    st.write("Ask about outfits, colour combinations, college looks, rainy-day dressing or styling your wardrobe.")
    st.caption("Powered by Google Gemini")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.markdown("**Try asking**")
    examples = [
        "What should I wear for college on Monday?",
        "Suggest a polished outfit for a presentation.",
        "How can I style black trousers?",
        "What should I avoid wearing on a rainy day?",
        "Does brown go with cream?",
    ]
    for example in examples:
        if st.button(example, use_container_width=True):
            st.session_state.pending_question = example

# Read the key from Streamlit secrets (.streamlit/secrets.toml).
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except (KeyError, FileNotFoundError):
    api_key = ""

if not api_key or api_key == "PASTE_YOUR_GEMINI_API_KEY_HERE":
    st.warning(
        "Add your Gemini API key in `.streamlit/secrets.toml` before starting the app. "
        "See README.txt included in the ZIP."
    )
    st.code('GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY"', language="toml")
    st.stop()

@st.cache_resource
def get_client(key: str):
    return genai.Client(api_key=key)

client = get_client(api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = ""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What would you like help styling today?")
if st.session_state.pending_question:
    prompt = st.session_state.pending_question
    st.session_state.pending_question = ""

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Putting together your look..."):
            try:
                # Include recent conversation turns so follow-up questions have context.
                history = []
                for item in st.session_state.messages[-10:]:
                    history.append(f'{item["role"].upper()}: {item["content"]}')
                conversation = "\n\n".join(history)

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=MANUAL + "\n\nConversation:\n" + conversation,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        temperature=0.7,
                    ),
                )
                answer = response.text or "I couldn't generate a response. Please try asking in another way."
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as exc:
                st.error(
                    "I couldn't connect to Gemini. Check your internet connection, "
                    "API key and model access, then try again."
                )
                st.caption(f"Technical details: {exc}")
