import React from "react";
import articulos from "../assets/articulos.png";
import LectorQr from "./LectorQr";

function Articulo() {
  return (
    <section>
      <div>
        <h1>Articulos</h1>
      </div>
      {/* <img style={{width: "500px"}} src={articulos} alt="articulo" /> */}
      <LectorQr />
    </section>
  );
}

export default Articulo;
