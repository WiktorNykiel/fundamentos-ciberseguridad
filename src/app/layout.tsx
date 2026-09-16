import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Fundamentos de ciberseguridad · Aplicación de referencia",
  description: "Aplicación de referencia. El campus estático se compila desde campus/.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  // The preserved reference page is English; the independent campus is Spanish.
  return <html lang="en"><body className="antialiased">{children}</body></html>;
}
