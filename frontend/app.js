const imageInput = document.getElementById("imageInput");
const removeBtn = document.getElementById("removeBtn");
const resultImage = document.getElementById("resultImage");
const downloadLink = document.getElementById("downloadLink");

removeBtn.addEventListener("click", async () => {
  const file = imageInput.files[0];

  if (!file) {
    alert("Veuillez sélectionner une image !");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://127.0.0.1:8001/remove-bg", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Erreur du serveur : ${response.status}`);
    }

    const blob = await response.blob();
    const imageUrl = URL.createObjectURL(blob);

    resultImage.src = imageUrl;
    downloadLink.href = imageUrl;
    downloadLink.style.display = "inline";
    downloadLink.download = "result.png"; // Nom du fichier téléchargé
  } catch (err) {
    console.error(err);
    alert("Une erreur est survenue lors de la suppression du fond.");
  }
});