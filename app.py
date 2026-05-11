import streamlit as st
from predictor import NextWordPredictor


st.set_page_config(
    page_title="Next Word Predictor",
    page_icon="🧠",
    layout="centered"
)


@st.cache_resource
def load_model():
    return NextWordPredictor()


def main():
    st.title("🧠 General Next Word Predictor")

    st.write(
        "Type any sentence, and the app will suggest likely next words. "
        "This version predicts based on the context you provide."
    )

    st.warning(
        "Privacy note: Do not enter private medical records, names, IDs, addresses, "
        "or sensitive personal information while testing."
    )

    predictor = load_model()

    user_text = st.text_area(
        "Enter your sentence:",
        placeholder="Example: This product will help customers",
        height=120
    )

    top_k = st.slider(
        "Number of word suggestions",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("Predict Next Words"):
        if not user_text.strip():
            st.error("Please enter a sentence first.")
            return

        with st.spinner("Generating suggestions..."):
            predictions = predictor.predict(user_text, top_k=top_k)

        if not predictions:
            st.error("No predictions found. Try writing a little more context.")
            return

        st.subheader("Suggested Next Words")

        cols = st.columns(min(len(predictions), 5))

        for i, pred in enumerate(predictions):
            with cols[i % len(cols)]:
                st.button(pred["word"])

        st.subheader("Prediction Details")

        for i, pred in enumerate(predictions, start=1):
            st.markdown(
                f"""
                **{i}. {pred['word']}**  
                Completed sentence: `{pred['completed_sentence']}`
                """
            )

    st.divider()

    st.subheader("Examples to try")

    st.code("This product will help customers")
    st.code("Our marketing strategy should focus on")
    st.code("The main benefit of this service is")
    st.code("I want to explain the value of")
    st.code("The client is interested in")
    st.code("The campaign performance improved because")


if __name__ == "__main__":
    main()
