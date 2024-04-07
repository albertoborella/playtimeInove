import React, { useState } from "react";
import QrReader from "react-qr-reader";
import styles from "../styles/LectorQr.module.css";
import QrCodeScannerIcon from "@mui/icons-material/QrCodeScanner";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

export default function LectorQr() {
  //Estados para  el resultado de lectura y para ternarios
  const [result, setResult] = useState("");
  const [camara, setCamara] = useState(false);
  /* console.log(QrReader); */

  //Esta funcion es la encargada de activar el scanner
  const handleScan = (data) => {
    if (data) {
      setResult(data);
      Reset();
    }
  };

  const handleError = (err) => {
    alert(err);
  };
  /* const handleScan = (data, error) => {
    if (data) {
      setResult(data);
      Reset();
    }

    if (error) {
      console.warn(error);
    }
  }; */
  const qrScanner = () => {
    setCamara(true);
    setResult("");
  };

  const Reset = () => {
    setCamara(false);
  };

  return (
    <div className={styles.padre}>
      <div className={styles.lectorQr}>
        <div>
          <div className={styles.posicionCancelScan}>
            <button
              hidden={camara ? "" : "hidden"}
              className={styles.cancelarScan}
              onClick={() => {
                Reset();
                setResult("");
              }}
            >
              X
            </button>
          </div>

          {camara ? (
            <QrReader
              delay={300}
              onError={handleError}
              onScan={handleScan}
              facingMode="environment"
              style={{
                width: "100vw",
                display: "flex",
                justofyContent: "center",
                alignItems: "center",
                /* paddingLeft: "-20px", */
              }}
            />
          ) : (
            <div className={styles.scanButton} hidden={result ? "hidden" : ""}>
              <QrCodeScannerIcon
                onClick={() => qrScanner()}
                sx={{
                  width: "fit-content",
                  fontSize: "10rem",
                  backgroundColor: "#d50000",
                  color: "white",
                  borderRadius: "30px",
                  padding: "20px",
                }}
              ></QrCodeScannerIcon>
              <p className={styles.p}>Escanear Qr</p>
            </div>

            /* <QRCodeSVG
              value={result == "" ? "www.playtime.com.ar" : result}
            ></QRCodeSVG> */
          )}
        </div>
      </div>
      <Card
        sx={{
          minWidth: 200,
          height: "fit-content",
          margin: 10,
          marginRadius: 10,
        }}
        hidden={result ? "" : "hidden"}
      >
        <CardContent>
          <Typography
            variant="h5"
            component="div"
            sx={{ width: 150, height: "fit-content" }}
          >
            {result}
          </Typography>
          <Typography variant="div">alguna caracteristica del item</Typography>
        </CardContent>
        <CardActions sx={{ display: "flex", justifyContent: "space-between" }}>
          <Button
            size="small"
            sx={{
              backgroundColor: "#d50000",
              color: "white",
              width: "fit-content",
              paddingLeft: 5,
              paddingRight: 5,
            }}
          >
            Ver mas
          </Button>
          <Button
            size="small"
            sx={{
              backgroundColor: "#d50000",
              color: "white",
              width: "fit-content",
            }}
            onClick={() => {
              Reset();
              setResult("");
            }}
          >
            X
          </Button>
        </CardActions>
      </Card>
      {/* <div className={styles.resultadoBox}>
        <p className={styles.resultado}>{result}</p>
        <div className={styles.detalleResultado}>
          <button
            hidden={result ? "" : "hidden"}
            style={{ backgroundColor: "#d50000", color: "white" }}
          >
            Ver mas
          </button>
        </div>
      </div> */}
    </div>
  );
}
