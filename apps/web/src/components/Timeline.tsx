"use client";

export interface Clip {
  id: string;
  name: string;
  duration: number;
  type: "video" | "audio" | "text";
}

interface TimelineProps {
  clips: Clip[];
}

export function Timeline({ clips }: TimelineProps) {
  return (
    <div style={{ border: "1px solid #ccc", padding: "1rem", borderRadius: "8px", background: "#f9f9f9" }}>
      <h3>Linha do Tempo de Edição</h3>
      {clips.length === 0 ? (
        <p style={{ color: "#666" }}>Nenhum clipe adicionado na timeline.</p>
      ) : (
        <div style={{ display: "flex", gap: "0.5rem", overflowX: "auto", padding: "0.5rem 0" }}>
          {clips.map((clip) => (
            <div
              key={clip.id}
              style={{
                minWidth: "120px",
                padding: "0.75rem",
                background: clip.type === "video" ? "#0070f3" : clip.type === "audio" ? "#10b981" : "#f59e0b",
                color: "#fff",
                borderRadius: "4px",
                textAlign: "center",
              }}
            >
              <div style={{ fontWeight: "bold", fontSize: "0.9rem" }}>{clip.name}</div>
              <div style={{ fontSize: "0.8rem", opacity: 0.9 }}>{clip.duration}s ({clip.type})</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
