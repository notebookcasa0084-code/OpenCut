export interface ProjectInput {
  name: string;
  fps?: number;
  resolution?: string;
}

export async function createProject(data: ProjectInput, apiUrl: string = "http://localhost:3000") {
  const response = await fetch(`${apiUrl}/projects`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error(`Failed to create project: ${response.statusText}`);
  }

  return response.json();
}
