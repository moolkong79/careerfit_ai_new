import { useState } from "react";

function InputForm({ onSubmit, isLoading }) {
  const [major, setMajor] = useState("");
  const [skillsInput, setSkillsInput] = useState("");
  const [jobType, setJobType] = useState("");

  function handleSubmit() {
    const skills = skillsInput
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);

    onSubmit({ major, skills, jobType });
  }

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
      <div className="mb-5">
        <h2 className="text-lg font-semibold text-slate-700">
          내 정보 입력
        </h2>
        <p className="mt-1 text-sm text-slate-500">
          전공, 보유 스킬, 관심 직무를 입력하면 CareerFit AI가 맞춤형 분석을 제공합니다.
        </p>
      </div>

      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-slate-600 mb-1">
            전공
          </label>
          <input
            type="text"
            value={major}
            onChange={(e) => setMajor(e.target.value)}
            placeholder="예: 통계학과, 경영학과, AI융합교육학"
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-slate-600 mb-1">
            보유 스킬
          </label>
          <input
            type="text"
            value={skillsInput}
            onChange={(e) => setSkillsInput(e.target.value)}
            placeholder="예: Python, SQL, R"
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <p className="mt-1 text-xs text-slate-500">
            쉼표로 구분해서 입력하세요.
          </p>
        </div>

        <div>
          <label className="block text-sm font-medium text-slate-600 mb-1">
            관심 직무
          </label>
          <input
            type="text"
            value={jobType}
            onChange={(e) => setJobType(e.target.value)}
            placeholder="예: 데이터 분석, 백엔드 개발, AI 사내강사"
            className="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <button
          type="button"
          onClick={handleSubmit}
          disabled={isLoading || !major || !skillsInput || !jobType}
          className="w-full bg-blue-500 hover:bg-blue-600 disabled:bg-slate-300 text-white font-medium py-2 px-4 rounded-lg transition-colors text-sm"
        >
          {isLoading ? "분석 중..." : "역량 분석 요청"}
        </button>
      </div>
    </div>
  );
}

export default InputForm;