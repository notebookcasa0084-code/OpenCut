export interface ProjectInput {
  name: string;
  fps?: number;
  resolution?: string;
}

export interface Project extends ProjectInput {
  id: string;
  createdAt?: string;
}

export async function getProjects(apiUrl: string = "http://localhost:3000"): Promise<Project[]> {
  const response = await fetch(`${apiUrl}/projects`);
  if (!response.ok) {
    throw new Error(`Failed to fetch projects: ${response.statusText}`);
  }
  const data = await response.json();
  return data.projects || [];
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
