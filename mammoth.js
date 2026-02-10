/*
  mammoth.js
  Dùng để load file .docx và hiển thị ra <code>
  Yêu cầu: đã load mammoth.browser.min.js
*/

async function loadDocxToCode(options) {
  const {
    filePath,
    codeElementId = "code",
    languageClass = "language-python"
  } = options;

  try {
    const response = await fetch(filePath);
    if (!response.ok) {
      throw new Error("Không tìm thấy file Word");
    }

    const arrayBuffer = await response.arrayBuffer();

    const result = await mammoth.extractRawText({ arrayBuffer });

    const codeEl = document.getElementById(codeElementId);
    if (!codeEl) {
      throw new Error("Không tìm thấy thẻ code");
    }

    codeEl.className = languageClass;
    codeEl.textContent = result.value;

    if (window.Prism) {
      Prism.highlightElement(codeEl);
    }

  } catch (err) {
    console.error(err);
    const codeEl = document.getElementById(codeElementId);
    if (codeEl) {
      codeEl.textContent = "❌ Lỗi đọc file Word: " + err.message;
    }
  }
}
