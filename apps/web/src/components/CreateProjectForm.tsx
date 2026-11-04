"use client";

import { useEffect, useState } from "react";
import { createProject, getProjects, Project } from "../services/api";

export function CreateProjectForm() {
  const [name, setName] = useState("");
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<string | null>(null);

  const fetchProjectsList = async () => {
    try {
      const list = await getProjects();
      setProjects(list);
    } catch (err) {
      console.error("Failed to load projects", err);
    }
  };

  useEffect(() => {
    fetchProjectsList();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;

    setLoading(true);
    setMessage(null);

    try {
      const result = await createProject({ name, fps: 60, resolution: "1080p" });
      setMessage(`Projeto "${result.project?.name || name}" criado com sucesso!`);
      setName("");
      await fetchProjectsList();
    } catch (err) {
      setMessage("Erro ao criar projeto.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "2rem", maxWidth: "500px" }}>
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
        <h2>Novo Projeto OpenCut</h2>
        <input
          type="text"
          placeholder="Nome do Projeto"
          value={name}
          onChange={(e) => setName(e.target.value)}
          disabled={loading}
          required
          style={{ padding: "0.5rem" }}
        />
        <button type="submit" disabled={loading} style={{ padding: "0.5rem" }}>
          {loading ? "Criando..." : "Criar Projeto"}
        </button>
        {message && <p>{message}</p>}
      </form>

      <div>
        <h3>Projetos Existentes ({projects.length})</h3>
        {projects.length === 0 ? (
          <p>Nenhum projeto cadastrado ainda.</p>
        ) : (
          <ul style={{ paddingLeft: "1.2rem" }}>
            {projects.map((p) => (
              <li key={p.id} style={{ marginBottom: "0.5rem" }}>
                <strong>{p.name}</strong> ({p.resolution}, {p.fps}fps)
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
