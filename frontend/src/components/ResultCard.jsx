// frontend/src/components/ResultCard.jsx

function SectionList({ title, items, badgeClassName }) {
  if (!items || items.length === 0) {
    return null;
  }

  return (
    <div className="mt-4 rounded-lg bg-slate-50 border border-slate-200 p-4">
      <h3 className="text-sm font-semibold text-slate-700 mb-2">{title}</h3>
      <div className="flex flex-wrap gap-2">
        {items.map((item, index) => (
          <span
            key={index}
            className={`rounded-full px-3 py-1 text-xs font-medium ${badgeClassName}`}
          >
            {item}
          </span>
        ))}
      </div>
    </div>
  );
}

function ResultCard({
  answer,
  matched_skills,
  missing_skills,
  recommended_projects,
  confidence,
}) {
  return (
    <div className="bg-white rounded-xl shadow-sm border-l-4 border-emerald-500 p-6">
      <div className="mb-4 flex items-start justify-between gap-4">
        <div>
          <h2 className="text-lg font-semibold text-slate-700">
            📊 AI 분석 결과
          </h2>
          <p className="mt-1 text-sm text-slate-500">
            입력한 전공, 스킬, 관심 직무를 바탕으로 분석한 결과입니다.
          </p>
        </div>

        {confidence !== undefined && confidence !== null && (
          <span className="shrink-0 rounded-full bg-emerald-50 px-3 py-1 text-xs font-medium text-emerald-700 border border-emerald-200">
            신뢰도 {confidence}
          </span>
        )}
      </div>

      <div className="rounded-lg bg-slate-50 border border-slate-200 p-4">
        <p className="text-slate-600 text-sm leading-relaxed whitespace-pre-line">
          {answer || "분석 결과가 없습니다."}
        </p>
      </div>

      <SectionList
        title="잘 맞는 역량"
        items={matched_skills}
        badgeClassName="bg-blue-50 text-blue-700 border border-blue-100"
      />

      <SectionList
        title="보완할 역량"
        items={missing_skills}
        badgeClassName="bg-red-50 text-red-700 border border-red-100"
      />

      <SectionList
        title="추천 프로젝트"
        items={recommended_projects}
        badgeClassName="bg-emerald-50 text-emerald-700 border border-emerald-100"
      />
    </div>
  );
}

export default ResultCard;