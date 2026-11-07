/* Path inputs stay in the browser and are never stored or sent. */
(() => {
  "use strict";
  function setup() {
    document.querySelectorAll("[data-path-command]").forEach((container) => {
      if (container.dataset.initialized) return;
      container.dataset.initialized = "true";
      const path = container.querySelector("[data-path]");
      const shell = container.querySelector("[data-shell]");
      const code = container.querySelector("[data-command]");
      const button = container.querySelector("[data-copy]");
      const language = container.querySelector("[data-language]");
      const status = container.querySelector("[data-status]");
      let timer;
      let version = 0;
      const valid = () => path.value.trim().length > 0 &&
        ![...path.value].some((char) => char.charCodeAt(0) < 32 || char.charCodeAt(0) === 127);
      const command = () => shell.value === "powershell"
        ? "Set-Location -LiteralPath '" + path.value.replaceAll("'", "''") + "'"
        : "cd -- '" + path.value.replaceAll("'", "'\\''") + "'";
      function update() {
        version++;
        clearTimeout(timer);
        const ready = valid();
        button.disabled = !ready;
        button.textContent = "Kopieren";
        path.setAttribute("aria-invalid", String(path.value.length > 0 && !ready));
        language.textContent = shell.value === "powershell" ? "PowerShell" : "Bash";
        code.textContent = ready ? command() :
          (shell.value === "powershell" ? "Set-Location -LiteralPath " : "cd -- ") + "[Vollständiger Ordnerpfad]";
        status.textContent = ready ? "" : path.value.length > 0
          ? "Einen Ordnerpfad ohne Zeilenumbrüche oder Steuerzeichen eingeben."
          : "Zuerst den Ordnerpfad eingeben.";
      }
      path.addEventListener("input", update);
      shell.addEventListener("change", update);
      button.addEventListener("click", async () => {
        if (!valid()) return;
        const revision = version;
        try {
          await navigator.clipboard.writeText(command());
          if (revision !== version) return;
          button.textContent = "Kopiert ✓";
          status.textContent = "Der fertige Befehl wurde kopiert.";
          timer = setTimeout(() => {
            button.textContent = "Kopieren";
            status.textContent = "";
          }, 2000);
        } catch {
          if (revision === version) status.textContent = "Kopieren nicht möglich. Den Befehl im Codeblock markieren und manuell kopieren.";
        }
      });
      update();
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
})();
