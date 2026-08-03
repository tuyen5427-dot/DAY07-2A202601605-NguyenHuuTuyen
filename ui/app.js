/* =========================================================
   UET K3 RAG Intelligence — Frontend JavaScript Logic
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {
    const searchForm = document.getElementById("searchForm");
    const queryInput = document.getElementById("queryInput");
    const kbStatus = document.getElementById("kbStatus");
    const benchmarkPills = document.querySelectorAll(".pill-btn");

    const answerPlaceholder = document.getElementById("answerPlaceholder");
    const answerLoading = document.getElementById("answerLoading");
    const answerContent = document.getElementById("answerContent");
    const answerText = document.getElementById("answerText");

    const chunksPlaceholder = document.getElementById("chunksPlaceholder");
    const chunksLoading = document.getElementById("chunksLoading");
    const chunksList = document.getElementById("chunksList");
    const retrievedCount = document.getElementById("retrievedCount");

    // 1. Check server status & KB chunks
    fetchStatus();

    async function fetchStatus() {
        try {
            const res = await fetch("/api/status");
            if (res.ok) {
                const data = await res.json();
                kbStatus.textContent = `${data.total_chunks} chunks loaded (${data.strategy})`;
            } else {
                kbStatus.textContent = "Offline / Error";
            }
        } catch (e) {
            kbStatus.textContent = "Demo / Offline Mode";
            console.warn("Could not connect to /api/status:", e);
        }
    }

    // 2. Handle Benchmark Quick-Select Pills
    benchmarkPills.forEach(pill => {
        pill.addEventListener("click", (e) => {
            e.preventDefault();
            // Remove active class from all
            benchmarkPills.forEach(p => p.classList.remove("active"));
            pill.classList.add("active");

            const query = pill.getAttribute("data-query");
            const filterVal = pill.getAttribute("data-filter");

            queryInput.value = query;

            // Set radio filter
            const radio = document.querySelector(`input[name="metaFilter"][value="${filterVal}"]`);
            if (radio) radio.checked = true;

            // Automatically trigger search
            performSearch(query, filterVal);
        });
    });

    // 3. Handle search form submit
    searchForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const query = queryInput.value.trim();
        if (!query) return;

        // Clear active pill if user types custom query
        benchmarkPills.forEach(p => p.classList.remove("active"));

        const filterVal = document.querySelector('input[name="metaFilter"]:checked')?.value || "";
        performSearch(query, filterVal);
    });

    // 4. Perform Search & Render Results
    async function performSearch(query, filterStr) {
        // Show loading state
        answerPlaceholder.classList.add("hidden");
        answerContent.classList.add("hidden");
        answerLoading.classList.remove("hidden");

        chunksPlaceholder.classList.add("hidden");
        chunksList.classList.add("hidden");
        chunksLoading.classList.remove("hidden");

        retrievedCount.textContent = "Searching...";

        // Parse filter
        let filterObj = null;
        if (filterStr && filterStr.includes(":")) {
            const [key, val] = filterStr.split(":");
            filterObj = { [key]: val };
        }

        try {
            const response = await fetch("/api/rag", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    query: query,
                    filter: filterObj,
                    top_k: 3
                })
            });

            if (!response.ok) {
                throw new Error(`Server returned HTTP ${response.status}`);
            }

            const data = await response.json();

            // Render Chunks
            renderChunks(data.results || []);

            // Render Answer with typewriter effect
            renderAnswer(data.answer || "Không có phản hồi từ AI.");

        } catch (error) {
            console.error("RAG Query Error:", error);
            answerLoading.classList.add("hidden");
            answerContent.classList.remove("hidden");
            answerText.textContent = `Lỗi kết nối tới máy chủ RAG: ${error.message}`;

            chunksLoading.classList.add("hidden");
            chunksPlaceholder.classList.remove("hidden");
            retrievedCount.textContent = "Error";
        }
    }

    // 5. Render Retrieved Chunks
    function renderChunks(chunks) {
        chunksLoading.classList.add("hidden");
        chunksList.innerHTML = "";

        if (!chunks || chunks.length === 0) {
            chunksPlaceholder.classList.remove("hidden");
            retrievedCount.textContent = "0 chunks";
            return;
        }

        retrievedCount.textContent = `${chunks.length} chunks retrieved`;
        chunksList.classList.remove("hidden");

        chunks.forEach((chunk, idx) => {
            const rankNum = idx + 1;
            const scoreFormatted = (typeof chunk.score === "number") ? chunk.score.toFixed(4) : chunk.score;
            const docId = chunk.metadata?.doc_id || chunk.id || "unknown";
            const textContent = chunk.content || "";

            const chunkItem = document.createElement("div");
            chunkItem.className = "chunk-item";
            chunkItem.id = `chunk-card-${rankNum}`;

            chunkItem.innerHTML = `
                <div class="chunk-header">
                    <div class="chunk-rank-doc">
                        <span class="chunk-rank">#${rankNum}</span>
                        <span class="chunk-doc-id">${docId}</span>
                    </div>
                    <div class="chunk-score-box">
                        <span class="score-badge">score: ${scoreFormatted}</span>
                    </div>
                </div>
                <div class="chunk-text">${escapeHtml(textContent)}</div>
            `;

            chunksList.appendChild(chunkItem);
        });
    }

    // 6. Render Answer with Typewriter Effect & Styled Citations
    function renderAnswer(rawText) {
        answerLoading.classList.add("hidden");
        answerContent.classList.remove("hidden");
        answerText.innerHTML = "";

        // Stylize citations like [1], [2] to interactive spans
        let formattedText = escapeHtml(rawText);
        formattedText = formattedText.replace(/\[(\d+)\]/g, (match, p1) => {
            return `<span class="citation-link" data-rank="${p1}" title="Click để làm nổi bật dẫn chứng #${p1}">[${p1}]</span>`;
        });

        // Typewriter animation
        let i = 0;
        const tempDiv = document.createElement("div");
        tempDiv.innerHTML = formattedText;
        const textToType = tempDiv.innerHTML;

        answerText.innerHTML = textToType;

        // Add interactive event listeners to citations
        document.querySelectorAll(".citation-link").forEach(link => {
            link.style.color = "var(--accent-cyan)";
            link.style.fontWeight = "700";
            link.style.cursor = "pointer";
            link.style.textDecoration = "underline";

            link.addEventListener("click", () => {
                const rank = link.getAttribute("data-rank");
                const targetCard = document.getElementById(`chunk-card-${rank}`);
                if (targetCard) {
                    targetCard.scrollIntoView({ behavior: "smooth", block: "center" });
                    targetCard.style.boxShadow = "0 0 25px rgba(56, 189, 248, 0.6)";
                    targetCard.style.borderColor = "var(--accent-cyan)";
                    setTimeout(() => {
                        targetCard.style.boxShadow = "";
                        targetCard.style.borderColor = "";
                    }, 2000);
                }
            });
        });
    }

    function escapeHtml(str) {
        return str
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
});
