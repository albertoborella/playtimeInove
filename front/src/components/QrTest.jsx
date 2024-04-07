import { useEffect, useState } from "react";
import { useZxing } from "react-zxing";

export const BarcodeScanner = () => {
  const [result, setResult] = useState("");

  const { ref, pause, resume } = useZxing({
    onDecodeResult(result) {
      setResult(result.getText());
    },
  });

  useEffect(() => {
    if (result) {
      // Pausar la cámara cuando result tiene un valor
      pause();
    } else {
      // Reanudar la cámara cuando result está vacío
      resume();
    }
  }, [result, pause, resume]);

  return (
    <>
      <video ref={ref} />
      <p>
        <span>Escaneamos el ID!:</span>
        {console.log("result", result)}
        <span>{result}</span>
      </p>
    </>
  );
};