import "./App.css";
import RouterPrincipal from "./router/RouterPrincipal";
import { useState } from "react";
import { Autorizacion, initAutenticacion } from "./context/AuthContext";
import Login from "./components/Login";

function App() {
  const [auth, setAuth] = useState(initAutenticacion());

  return (
    <>
      <Autorizacion.Provider value={{  auth, setAuth  }}>
        {auth ? (
          <div className="App">
            <RouterPrincipal auth={auth}/>
          </div>
        ) : <Login/>}
      </Autorizacion.Provider>
    </>
  );
}

export default App;
