console.log("TMCLibrary loaded");

const searchInput = document.querySelector(".search");
const cards = document.querySelectorAll(".card");

searchInput.addEventListener("input", () => {
    const value = searchInput.value.toLowerCase();
    cards.forEach(card => {
        card.style.display = card.innerText.toLowerCase().includes(value)
            ? "block"
            : "none";
    });
});

function copyCode() {
  const text = document.getElementById("code").innerText;
  navigator.clipboard.writeText(text);

  const toast = document.getElementById("toast");
  toast.classList.add("show");

  setTimeout(() => {
    toast.classList.remove("show");
  }, 2000);
}
