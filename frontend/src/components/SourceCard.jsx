// frontend/src/components/SourceCard.jsx

function formatDistance(distance) {
  if (distance === undefined || distance === null || distance === "") {
    return "정보 없음";
  }

  const numberDistance = Number(distance);

  if (Number.isNaN(numberDistance)) {
    return distance;
  }

  return numberDistance.toFixed(4);
}

function SourceCard({ sources }) {
  if (!sources || sources.length === 0) {
    return (
      <div className="bg-slate-50 rounded-xl border border-slate-200 p-4 text-sm text-slate-500">
        참고한 공고 데이터가 없습니다.
      </div>
    );
  }

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
      <div className="mb-4">
        <h2 className="text-lg font-semibold text-slate-700">
          📄 참고한 공고 출처
        </h2>
        <p className="mt-1 text-sm text-slate-500">
          AI 답변 생성에 참고된 ChromaDB 검색 결과입니다.
        </p>
      </div>

      <div className="space-y-3">
        {sources.map((source, index) => (
          <div
            key={index}
            className="rounded-lg border border-slate-200 bg-slate-50 p-4"
          >
            <div className="flex items-start justify-between gap-3">
              <div>
                <p className="text-sm font-semibold text-slate-700">
                  {source.company || "회사명 없음"}
                </p>
                <p className="mt-1 text-sm text-slate-600">
                  {source.title || "공고명 없음"}
                </p>
              </div>

              {source.is_startup === "true" && (
                <span className="shrink-0 rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-medium text-emerald-700 border border-emerald-200">
                  스타트업
                </span>
              )}
            </div>

            <div className="mt-3 grid grid-cols-1 gap-2 text-xs text-slate-500 sm:grid-cols-2">
              <p>
                <span className="font-medium text-slate-600">직무유형:</span>{" "}
                {source.job_type || "정보 없음"}
              </p>

              <p>
                <span className="font-medium text-slate-600">마감일:</span>{" "}
                {source.deadline || "정보 없음"}
              </p>

              <p>
                <span className="font-medium text-slate-600">마감월:</span>{" "}
                {source.deadline_month || "정보 없음"}
              </p>

              <p>
                <span className="font-medium text-slate-600">검색 거리:</span>{" "}
                {formatDistance(source.distance)}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SourceCard;