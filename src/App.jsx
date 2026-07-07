// frontend/src/App.jsx

import { useState } from "react";
import InputForm from "./components/InputForm";
import ResultCard from "./components/ResultCard";
import SourceCard from "./components/SourceCard";

const API_BASE = "http://localhost:8000";
// API Key는 절대 여기에 넣지 않습니다.

function App() {
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleAnalyze(formData) {
    setIsLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch(`${API_BASE}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          major: formData.major,
          skills: formData.skills,
          job_type: formData.jobType,
        }),
      });

      if (!response.ok) {
        let errorMessage = `서버 오류: ${response.status}`;

        try {
          const errorData = await response.json();
          if (errorData.detail) {
            errorMessage = `서버 오류: ${errorData.detail}`;
          }
        } catch {
          // 서버가 JSON이 아닌 에러를 줄 수도 있으므로 무시
        }

        throw new Error(errorMessage);
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      if (err.message.includes("Failed to fetch")) {
        setError(
          "FastAPI 서버에 연결할 수 없습니다. backend에서 uvicorn 서버가 실행 중인지 확인하세요."
        );
      } else {
        setError(err.message);
      }
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-slate-50 py-10 px-4">
      <div className="max-w-2xl mx-auto">
        <header className="mb-8">
          <h1 className="text-2xl font-bold text-slate-800">
            CareerFit AI
          </h1>
          <p className="mt-2 text-sm text-slate-500">
            취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치
          </p>
        </header>

        <InputForm onSubmit={handleAnalyze} isLoading={isLoading} />

        {error && (
          <div className="mt-4 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-700">
            {error}
          </div>
        )}

        {isLoading && (
          <div className="mt-8 rounded-xl border border-slate-200 bg-white p-6 text-center text-sm text-slate-500">
            분석 중입니다...
          </div>
        )}

        {result && (
          <div className="mt-8 space-y-4">
            <ResultCard
              answer={result.answer}
              matched_skills={result.matched_skills}
              missing_skills={result.missing_skills}
              recommended_projects={result.recommended_projects}
              confidence={result.confidence}
            />

            <SourceCard sources={result.sources} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;