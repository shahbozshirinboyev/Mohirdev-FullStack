const randomNumber = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1) + min);
};

const generateRandomNumber = () => {
  const minEl = document.getElementById("min");
  const maxEl = document.getElementById("max");

  if (minEl.value === "" || maxEl.value === "") {
    const toastLiveExample = document.getElementById("empetyNumbers");
    const toastBootstrap =
      bootstrap.Toast.getOrCreateInstance(toastLiveExample);
    toastBootstrap.show();
    return;
  }

  const min = Number(minEl.value);
  const max = Number(maxEl.value);

  if (min > max) {
    const toastLiveExample = document.getElementById("errorNumbers");
    const toastBootstrap =
      bootstrap.Toast.getOrCreateInstance(toastLiveExample);
    toastBootstrap.show();
    return;
  }

  const resultDisplay = document.getElementById("result");
  resultDisplay.textContent = randomNumber(min, max);
};

const generateBtn = document.getElementById("generate-btn");
generateBtn.addEventListener("click", generateRandomNumber);
