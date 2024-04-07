import { createContext } from "react";

//Contexto creado para la autorizacion del usuario

const AuthUser={
    auth: false,
}

export const Autorizacion = createContext(AuthUser);

export function initAutenticacion() {
    const isAuthenticated = sessionStorage.getItem("isAuthenticated");
    return Boolean(isAuthenticated); // Forzar que el dato sea interpretado como true/false (boolean)
  }
