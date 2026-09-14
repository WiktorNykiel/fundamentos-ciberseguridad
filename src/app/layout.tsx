import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Fundamentos de ciberseguridad · Aplicación de referencia",
  description: "Aplicación de referencia. El campus estático se compila desde campus/.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body
        className="antialiased"
      >
        {children}
      </body>
    </html>
  );
}
