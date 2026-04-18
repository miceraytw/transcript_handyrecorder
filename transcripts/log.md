# Log

## [2026-04-18] bootstrap | initialize handyrecorder transcript wiki
- Added `AGENTS.md`
- Added starter `wiki/` structure for mixed personal archive content
- Defined ingest, re-ingest, and lint workflow for speeches, family audio, meetings, and practice recordings

## [2026-04-18] batch ingest | 5 representative transcripts
- Created source notes for one speech, one family conversation, one music practice clip, one medical lecture, and one meeting transcript
- Added starter domain pages for family, speeches, medical talks, meetings, and music practice
- Added starter people pages and low-signal handling guidance
- Updated `wiki/index.md`

## [2026-04-18] batch ingest | 10 speech and medical transcripts
- Added 10 source notes centered on cell therapy, facelift lectures, medical-law forum remarks, and one microsurgery lecture
- Added `wiki/patterns/細胞治療法規與製程` and `wiki/patterns/拉皮手術設計與風險`
- Updated `wiki/domains/演講與簡報`, `wiki/domains/醫療與學術內容`, and `wiki/domains/會議與討論`
- Updated `wiki/home.md` and `wiki/index.md`

## [2026-04-18] lint | speech pages
- Tightened the speech domain into high-signal lectures, supporting fragments, and low-signal background remarks
- Lowered confidence for ceremonial / opening remarks that should not support technical conclusions
- Added explicit evidence posture to `wiki/patterns/細胞治療法規與製程` and `wiki/patterns/拉皮手術設計與風險`
- Updated low-signal handling rules for speech-like opening remarks

## [2026-04-18] batch ingest | 10 family transcripts
- Added 10 family-oriented source notes focused on bedtime, object boundaries, cleanup rules, departure pressure, and high-tension parent-child conflict
- Added `wiki/patterns/家庭衝突與調停`
- Updated `wiki/domains/家庭對話`, `wiki/people/abo`, and `wiki/people/孫時語`
- Updated `wiki/home.md` and `wiki/index.md`

## [2026-04-18] lint | family pages
- Added evidence posture to `wiki/domains/家庭對話` and `wiki/patterns/家庭衝突與調停`
- Lowered confidence for short family fragments and high-repetition high-tension transcripts that should only support pattern-level observations
- Updated low-signal rules to cover short family interaction clips

## [2026-04-18] batch ingest | practice and performance transcripts
- Added 10 source notes covering piano intros, singing, storytelling performance attempts, parent prompting, re-recording, and home practice constraints
- Added `wiki/patterns/表演前導與家庭式練習`
- Added `wiki/people/孫時晴`
- Updated `wiki/domains/音樂練習與表演`, `wiki/people/孫時語`, `wiki/people/abo`, `wiki/home.md`, and `wiki/index.md`

## [2026-04-18] lint | practice and performance pages
- Split the practice/performance group into fuller intro frames, mid-signal process clips, and low-signal intro-only examples
- Added evidence posture to `wiki/patterns/表演前導與家庭式練習`
- Updated low-signal rules for ultra-short performance intro clips

## [2026-04-18] batch ingest | learning and schoolwork transcripts
- Added a new domain `wiki/domains/學習與課業`
- Added source notes for English showcase intros, social studies hosting, reading homework support, geography video class interaction, tour-guide style oral output, and one short English presentation ending
- Added `wiki/patterns/課業展示與朗讀輔導`
- Updated `wiki/people/孫時語`, `wiki/people/abo`, `wiki/home.md`, and `wiki/index.md`

## [2026-04-18] lint | learning and schoolwork pages
- Split the learning/schoolwork group into fuller homework/showcase sources, mid-signal oral-output sources, and low-signal intro/outro-only examples
- Added evidence posture to `wiki/patterns/課業展示與朗讀輔導`
- Updated low-signal rules for ultra-short learning showcase clips

## [2026-04-18] batch ingest | early performance and school-output transcripts
- Added a local Telegram helper script at `/Users/sunray/codex/transcript_handyrecorder/notify_telegram.py` that reuses `/Users/sunray/newsbot/.env`
- Added 10 early source notes covering nursery-rhyme fragments, applause prompts, story intros, re-record prompts, hand-position correction, object presentations, and intro-only school-output clips
- Expanded `wiki/patterns/表演前導與家庭式練習` and `wiki/patterns/課業展示與朗讀輔導`
- Updated people pages for `孫時語` and `孫時晴`

## [2026-04-18] batch ingest | early family and storytelling transcripts
- Added 5 source notes covering beach/outing hesitation, getting-ready flow, broken-object accountability, sibling creative scoring play, and one long improvised story narration
- Expanded `wiki/domains/家庭對話` with outing-prep and trying-new-things interaction patterns
- Expanded `wiki/domains/音樂練習與表演` and `wiki/patterns/表演前導與家庭式練習` to include storytelling as part of the family performance archive
- Updated `wiki/patterns/家庭衝突與調停`, `wiki/people/abo`, and `wiki/index.md`

## [2026-04-18] batch ingest | short performance and oral-output transcripts
- Added 5 source notes covering recorder-use prompting, story performance with live coaching, body-part song output, one intro-only school-topic presentation, and one retry/correction clip
- Expanded `wiki/patterns/表演前導與家庭式練習` with coaching-language and retry prompts as first-class evidence
- Expanded `wiki/domains/學習與課業` and `wiki/patterns/課業展示與朗讀輔導` with short school-topic intro examples
- Updated `wiki/people/孫時晴`

## [2026-04-18] batch ingest | early facelift conference transcripts
- Added 4 source notes from the 20170604 facelift meeting, covering one opening/background segment, two technical/method talks, and one case discussion
- Expanded `wiki/domains/演講與簡報` to treat multi-part conference recordings as one event context instead of isolated clips
- Expanded `wiki/patterns/拉皮手術設計與風險` with midface / malar fat pad / volume tradeoff language from earlier facelift talks
- Updated `wiki/index.md`

## [2026-04-18] batch ingest | more facelift lecture and Q&A transcripts
- Added 4 more source notes from the 20170604 facelift meeting, covering individualized planning, comprehensive rejuvenation concepts, liposuction/dissection Q&A, and one expectation-setting prompt about longevity
- Expanded `wiki/domains/會議與討論` so facelift Q&A now explicitly carries patient-selection, revision-timing, and technical tradeoff value
- Expanded `wiki/patterns/拉皮手術設計與風險` with skin-thickness preservation, liposuction caution, and broader facial rejuvenation framing

## [2026-04-18] batch ingest | facelift meeting tail-end technical fragments
- Added 2 source notes from the tail end of the 20170604 facelift meeting, focused on plane finding, thickness handling, plication, and how neck / nasolabial concerns are judged in practice
- Marked two remaining 20170604 clips as low-signal rather than forcing ingestion
- Expanded `wiki/patterns/拉皮手術設計與風險` and `wiki/patterns/錄音品質與低訊號檔案`
