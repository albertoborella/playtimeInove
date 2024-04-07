import React from "react";
import stock from "../assets/stock.png";

function Stock() {
  return (
    <section>
      <div><h1>Stock</h1></div>
      <img style={{width: "500px"}} src={stock} alt="" />
    </section>
  );
}

export default Stock;
