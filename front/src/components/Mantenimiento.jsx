import React, { useEffect, useState } from "react";
import "../styles/mantenimiento.css";
import BuildIcon from "@mui/icons-material/Build";
import ConstructionIcon from "@mui/icons-material/Construction";
import AccessTimeIcon from "@mui/icons-material/AccessTime";

function Mantenimiento() {
  const [currentTime, setCurrentTime] = useState("00:00:00");

  useEffect(() => {
    // Lógica para obtener y actualizar la hora actual cada segundo
    const intervalId = setInterval(() => {
      const now = new Date();
      const hours = now.getHours().toString().padStart(2, "0");
      const minutes = now.getMinutes().toString().padStart(2, "0");
      const seconds = now.getSeconds().toString().padStart(2, "0");
      setCurrentTime(`${hours}:${minutes}:${seconds}`);
    }, 1000);

    return () => clearInterval(intervalId); // Limpia el intervalo al desmontar el componente
  }, []);

  return (
    <div >
      <div className="mantenimiento">
        <h1>Página web en construcción</h1>
        <p>
          Lo sentimos, no hemos encontrado un mensaje más original para decirte
          que estamos trabajando en ello.
        </p>
        <AccessTimeIcon style={{ fontSize: "65px" }} />
        <h2> Web disponible en:</h2>
        <p className="casio" id="reloj">
          {currentTime}
        </p>
      </div>
    </div>
  );
}

export default Mantenimiento;
