"use client";

import { useState } from "react";
import { createProject } from "../services/api";

export function CreateProjectForm() {
  const [name, setName] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;

    setLoading(true);
    setMessage(null);

    try {
      const result = await createProject({ name, fps: 60, resolution: "1080p" });
      setMessage(`Projeto "${result.project?.name || name}" criado com sucesso!`);
      setName("");
    } catch (err) {
      setMessage("Erro ao criar projeto.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "1rem", maxWidth: "400px" }}>
      <h2>Novo Projeto OpenCut</h2>
      <input
        type="text"
        placeholder="Nome do Projeto"
        value={name}
        onChange={(e) => setName(e.target.value)}
        disabled={loading}
        required
      />
      <button type="submit" disabled={loading}>
        {loading ? "Criando..." : "Criar Projeto"}
      </button>
      {message && <p>{message}</p>}
    </form>
  );
}
