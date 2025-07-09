const fetchTranslation = async (sourceLanguage) => {
  const response = await fetch("/translate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: sourceLanguage.value,
    }),
  });

  const data = await response.json();

  return data;
};

document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const { sourceLanguage } = form.elements;

    fetchTranslation(sourceLanguage)
      .then((targetLanguage) => {
        const result = document.getElementById("result");
        result.textContent = targetLanguage.text;
      })
      .catch((error) => {
        console.error("Translation error:", error);
      });
  });
});
