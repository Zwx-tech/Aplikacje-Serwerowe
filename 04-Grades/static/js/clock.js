function updateClock() {
  const date = new Date();
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');

  const timeElement = document.getElementById("time");
  timeElement.textContent = `${hours}:${minutes}:${seconds}`;
}
updateClock()
setInterval(updateClock, 1000);