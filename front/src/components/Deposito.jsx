import React from "react";
import deposito from "../assets/deposito.png";

function Deposito() {
  return (
    <section>
      <div>
        <h1>Depósito</h1>
      </div>
      <img style={{ width: "500px" }} src={deposito} alt="" />
    </section>
  );
}

export default Deposito;
