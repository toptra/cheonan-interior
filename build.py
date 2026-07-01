# -*- coding: utf-8 -*-
"""
천안인테리어 서브페이지 생성기
- 업체 입점 시 바꾸는 값은 CONFIG 한 곳에만: 다시 실행하면 8장 전체 갱신
- 각 페이지는 고유 콘텐츠(중복패널티 방지)
- 공용 디자인은 /assets/css/subpage.css 하나로 통일
"""
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────
# CONFIG : 업체 입점하면 여기만 바꾸고 재실행
# ─────────────────────────────────────────────
CONFIG = {
    "domain":     "https://cheonaninterior.daewoonai.com",
    "biz":        "천안인테리어",
    "phone":      "010-8672-3426",
    "phone_intl": "+82-10-8672-3426",
    "og_image":   "https://cheonaninterior.daewoonai.com/images/og-image.jpg",
    "ad_link":    "/#ad",
}
D = CONFIG["domain"]

# 푸터 링크(전 페이지 공통)
FOOTER_COLS = [
    ("인테리어 분야", [
        ("/cheonan-office-interior", "천안 사무실 인테리어"),
        ("/cheonan-apart-interior",  "천안 아파트 인테리어"),
        ("/cheonan-kitchen-interior","천안 주방 인테리어"),
        ("/cheonan-bathroom-interior","천안 욕실 인테리어"),
    ]),
    ("정보", [
        ("/cheonan-remodeling",        "천안 리모델링"),
        ("/cheonan-interior-cost",     "천안 인테리어 비용"),
        ("/cheonan-interior-portfolio","천안 시공 사례"),
        ("/cheonan-interior-faq",      "자주 묻는 질문"),
    ]),
]

# ─────────────────────────────────────────────
# 페이지 데이터 (각각 고유 콘텐츠)
# ─────────────────────────────────────────────
PAGES = []

def unsplash(pid, w=1400):
    return f"https://images.unsplash.com/photo-{pid}?w={w}&q=80"

# 1) 사무실
PAGES.append(dict(
    slug="cheonan-office-interior", label="Office Interior · 천안",
    h1="천안 사무실 인테리어",
    title="천안 사무실 인테리어 - 천안 오피스·사무실 리모델링·공유오피스",
    desc="천안 사무실 인테리어 전문 정보. 천안 오피스 인테리어, 사무실 리모델링, 공유오피스·병의원·학원 인테리어의 시공 범위와 평당 비용 기준, 불당동·두정동·서북구 등 천안 지역별 오피스 상권 특성을 안내합니다.",
    keywords="천안사무실인테리어,천안오피스인테리어,천안사무실리모델링,천안공유오피스인테리어,천안병원인테리어,천안학원인테리어,천안불당동사무실인테리어,천안서북구인테리어",
    hero=unsplash("1497366811353-6870744d04b2"), hero_alt="천안 사무실 인테리어 시공 사례 - 모던 오피스 공간",
    serviceType=["사무실인테리어","오피스인테리어","사무실리모델링","공유오피스인테리어","병원인테리어","학원인테리어"],
    aeo="<strong>천안 사무실 인테리어</strong>는 소규모 오피스부터 공유오피스, 병의원, 학원, 사옥까지 업무 공간의 목적에 맞춰 바닥·천장·조명·파티션·전기/데이터 배선·냉난방을 설계·시공하는 작업입니다. 천안 지역 기준 평당 <strong>60~120만 원</strong> 선이며, 부분 시공은 낮고 전체 리모델링은 높아집니다. 규모에 따라 1~4주가 소요됩니다.",
    body="""
<h2>천안 사무실 인테리어의 종류</h2>
<p>같은 "사무실"이라도 업종과 인원, 방문 고객 유무에 따라 방향이 완전히 달라집니다. 천안에서 자주 의뢰되는 유형입니다.</p>
<div class="feature-grid">
  <div class="feature-card"><p class="fc-num">01</p><h3>소규모 오피스</h3><p>10~30평 스타트업·1인 기업·지사. 파티션과 수납, 브랜드 컬러 중심의 효율 설계가 핵심입니다.</p></div>
  <div class="feature-card"><p class="fc-num">02</p><h3>공유오피스·사옥</h3><p>다수 입주사를 위한 회의실·라운지·개별 부스. 동선 분리와 방음, 공용부 완성도가 중요합니다.</p></div>
  <div class="feature-card"><p class="fc-num">03</p><h3>병의원·클리닉</h3><p>대기실·진료실·처치실의 위생 자재와 감염 관리 동선, 의료법 요건을 반영한 전문 시공이 필요합니다.</p></div>
  <div class="feature-card"><p class="fc-num">04</p><h3>학원·교육 공간</h3><p>강의실 방음·채광·안전 마감이 중심. 학부모 대기·상담 공간의 분위기도 등록률에 영향을 줍니다.</p></div>
</div>
<h2>천안 사무실 인테리어 시공 범위</h2>
<p>오피스는 마감뿐 아니라 <strong>전기·데이터·냉난방 설비</strong>가 함께 맞물려야 완성됩니다.</p>
<ul class="spec-list">
  <li><b>바닥</b> — 데코타일·강마루·카펫타일·에폭시 등 용도별 마감</li>
  <li><b>천장·조명</b> — 텍스·노출천장·라인조명으로 밝기와 분위기 조정</li>
  <li><b>파티션·벽체</b> — 유리 파티션·경량 칸막이·방음벽으로 공간 분할</li>
  <li><b>전기·데이터</b> — 콘센트·랜·서버 배선 신설/증설, 회의실 전원 정리</li>
  <li><b>냉난방·환기</b> — 시스템에어컨·환기 설비·공간별 온도 분리</li>
</ul>
<h2>천안 지역별 오피스 상권 특성</h2>
<div class="region-grid">
  <div class="region-card"><h3>불당동 · 불당신도시</h3><p>신축 오피스·병의원·학원 밀집. 완성도 높은 브랜드형 인테리어 수요가 많습니다.</p></div>
  <div class="region-card"><h3>두정동 · 성정동</h3><p>천안역·터미널 인근 전통 상권. 리모델링·부분 개선 수요가 꾸준합니다.</p></div>
  <div class="region-card"><h3>쌍용동 · 서북구</h3><p>주거·업무 혼합 지역. 소규모 오피스·지사·상담 공간 문의가 많습니다.</p></div>
  <div class="region-card"><h3>동남구 · 아산 인접권</h3><p>천안아산역 생활권. 출장 상담이 함께 이뤄지는 지역입니다.</p></div>
</div>
<h2>진행 절차</h2>
<ul class="spec-list">
  <li><b>1. 상담·현장 실측</b> — 평수·업종·예산·일정 확인</li>
  <li><b>2. 설계·견적</b> — 도면·3D 시안과 항목별 견적</li>
  <li><b>3. 시공</b> — 철거→설비→마감, 공정별 점검</li>
  <li><b>4. 준공·검수</b> — 하자 점검 후 인수, A/S 안내</li>
</ul>
""",
    faq=[
      ("천안 사무실 인테리어 비용은 평당 얼마인가요?","천안 사무실 인테리어 비용은 일반적으로 평당 60~120만 원 선입니다. 바닥·조명 위주 부분 시공은 낮고, 파티션·전기·냉난방까지 포함하는 전체 시공은 높아집니다. 정확한 금액은 현장 실측 후 견적으로 확인하는 것이 좋습니다."),
      ("공사 기간은 얼마나 걸리나요?","10~30평 소규모 오피스는 보통 1~2주, 설비까지 포함한 전체 리모델링은 3~4주가량 걸립니다. 밀집 건물은 관리사무소 공사 협의와 소음 시간대를 미리 확인하면 일정이 안정적입니다."),
      ("영업 중인 사무실도 시공 가능한가요?","가능합니다. 야간·주말 공사, 구역 분할 시공으로 업무 중단을 최소화합니다. 병의원·학원처럼 운영이 계속돼야 하는 공간은 공정을 나눠 진행합니다."),
      ("천안 어느 지역까지 시공하나요?","천안 서북구(불당·두정·성정·쌍용)와 동남구 전역, 인접한 아산시까지 상담 가능합니다."),
    ],
    related=["cheonan-apart-interior","cheonan-remodeling","cheonan-interior-cost"],
))

# 2) 아파트
PAGES.append(dict(
    slug="cheonan-apart-interior", label="Apartment · 천안",
    h1="천안 아파트 인테리어",
    title="천안 아파트 인테리어 - 천안 아파트 리모델링·올수리·부분시공",
    desc="천안 아파트 인테리어 전문 정보. 평형별 리모델링 범위, 신축 입주 vs 구축 올수리 차이, 확장·샷시·도배·마루 시공과 평당 비용 기준, 불당·백석·쌍용 등 천안 대단지 특성을 안내합니다.",
    keywords="천안아파트인테리어,천안아파트리모델링,천안아파트올수리,천안입주청소인테리어,천안24평인테리어,천안34평인테리어,천안불당동아파트인테리어,천안백석동인테리어",
    hero=unsplash("1600607687939-ce8a6c25118c"), hero_alt="천안 아파트 인테리어 시공 사례 - 모던 거실 리모델링",
    serviceType=["아파트인테리어","아파트리모델링","도배","마루시공","샷시","확장공사"],
    aeo="<strong>천안 아파트 인테리어</strong>는 신축 입주 전 부분 시공부터 구축 아파트 전체 올수리까지 범위가 넓습니다. 도배·마루·조명 위주면 평당 <strong>50~90만 원</strong>, 주방·욕실·샷시·확장까지 포함한 올수리는 평당 <strong>90~150만 원</strong>대가 일반적이며, 24·34·44평 등 평형과 노후도에 따라 달라집니다.",
    body="""
<h2>신축 입주 vs 구축 올수리</h2>
<p>천안 아파트 인테리어는 크게 두 갈래입니다. 어느 쪽인지에 따라 예산과 공정이 완전히 갈립니다.</p>
<div class="feature-grid">
  <div class="feature-card"><p class="fc-num">01</p><h3>신축 입주 전 시공</h3><p>도배·바닥·조명·붙박이 정도의 포인트 시공. 기본 마감이 살아 있어 비용이 상대적으로 낮습니다.</p></div>
  <div class="feature-card"><p class="fc-num">02</p><h3>구축 전체 올수리</h3><p>주방·욕실 교체, 샷시·확장, 전기·배관까지. 노후 배관·누수 점검이 함께 들어가 예산이 큽니다.</p></div>
</div>
<h2>평형별 시공 범위</h2>
<ul class="spec-list">
  <li><b>20평대(24·25평)</b> — 신혼·소형 가구. 수납 극대화와 밝은 톤의 공간 확장 연출</li>
  <li><b>30평대(33·34평)</b> — 천안에서 가장 수요가 많은 국민평형. 주방·거실 동선 개선이 핵심</li>
  <li><b>40평대 이상</b> — 파우더룸·드레스룸·아일랜드 주방 등 공간 분화 설계</li>
</ul>
<h2>주요 시공 항목</h2>
<ul class="spec-list">
  <li><b>도배·바닥</b> — 실크벽지, 강마루·강화마루·장판</li>
  <li><b>주방·욕실</b> — 상하부장·상판 교체, 타일·도기·방수</li>
  <li><b>샷시·확장</b> — 발코니 확장, 이중창 교체로 단열·결로 개선</li>
  <li><b>전기·조명</b> — 매입등·간접조명, 콘센트 위치 재배치</li>
</ul>
<h2>천안 대단지 특성</h2>
<div class="region-grid">
  <div class="region-card"><h3>불당동 · 백석동</h3><p>신축·준신축 대단지. 입주 전 포인트 시공과 스타일링 수요가 많습니다.</p></div>
  <div class="region-card"><h3>쌍용동 · 신방동</h3><p>준공 20년 안팎 단지 밀집. 전체 올수리·샷시 교체 문의가 꾸준합니다.</p></div>
  <div class="region-card"><h3>두정동 · 성성지구</h3><p>재정비·신규 입주가 섞인 지역. 평형별 맞춤 시공이 많습니다.</p></div>
  <div class="region-card"><h3>동남구 구도심</h3><p>노후 아파트 중심. 배관·전기까지 포함한 근본 리모델링이 필요한 곳이 많습니다.</p></div>
</div>
""",
    faq=[
      ("천안 34평 아파트 올수리 비용은 얼마인가요?","자재 등급과 시공 범위에 따라 다르지만 주방·욕실·샷시·확장까지 포함한 전체 올수리는 평당 90~150만 원 선에서 형성됩니다. 도배·바닥 위주 부분 시공이면 크게 낮아집니다. 정확한 금액은 실측 견적이 필요합니다."),
      ("입주 전 시공은 며칠 걸리나요?","도배·바닥·조명 위주 포인트 시공은 3~7일, 주방·욕실까지 포함하면 2~3주가량 걸립니다. 입주일 역산해 일정을 잡는 것이 중요합니다."),
      ("살면서(거주 중) 부분 시공도 가능한가요?","가능합니다. 도배·조명 교체나 욕실 한 곳만 등 부분 시공은 거주 상태에서도 진행합니다. 다만 전체 올수리는 이사 후 빈 집 상태가 효율적입니다."),
      ("샷시(창호) 교체만 따로 할 수 있나요?","네. 단열·결로·소음 개선을 위해 샷시만 교체하는 경우도 많습니다. 발코니 확장과 함께 진행하면 시공이 효율적입니다."),
    ],
    related=["cheonan-kitchen-interior","cheonan-bathroom-interior","cheonan-interior-cost"],
))

# 3) 주방
PAGES.append(dict(
    slug="cheonan-kitchen-interior", label="Kitchen · 천안",
    h1="천안 주방 인테리어",
    title="천안 주방 인테리어 - 천안 주방 리모델링·싱크대·상판 교체",
    desc="천안 주방 인테리어 전문 정보. ㅡ자·ㄷ자·아일랜드 주방 구조, 상하부장·상판(인조대리석·세라믹) 자재, 후드·타일·조명, 부분 교체 vs 전체 리모델링 비용 기준을 안내합니다.",
    keywords="천안주방인테리어,천안주방리모델링,천안싱크대교체,천안주방상판교체,천안아일랜드주방,천안주방타일,천안부엌인테리어",
    hero=unsplash("1556909114-f6e7ad7d3136"), hero_alt="천안 주방 인테리어 시공 사례 - 모던 아일랜드 주방",
    serviceType=["주방인테리어","주방리모델링","싱크대교체","상판교체","타일시공"],
    aeo="<strong>천안 주방 인테리어</strong>는 싱크대·상판 부분 교체부터 구조를 바꾸는 전체 리모델링까지 범위가 다양합니다. 상하부장·상판 교체 중심이면 <strong>150~400만 원</strong>, 타일·바닥·전기·후드까지 포함한 전체 리모델링은 <strong>500~1,000만 원</strong> 이상으로, 주방 크기와 자재 등급에 따라 달라집니다.",
    body="""
<h2>주방 구조별 특징</h2>
<div class="feature-grid">
  <div class="feature-card"><p class="fc-num">01</p><h3>ㅡ자형</h3><p>한 벽면에 배치. 소형 평형·원룸에 적합하고 비용이 가장 낮습니다.</p></div>
  <div class="feature-card"><p class="fc-num">02</p><h3>ㄱ·ㄷ자형</h3><p>동선이 짧아 작업 효율이 높은 구조. 30평대 아파트에서 가장 흔합니다.</p></div>
  <div class="feature-card"><p class="fc-num">03</p><h3>아일랜드형</h3><p>중앙 조리대로 개방감과 수납을 동시에. 넓은 주방·거실 통합형에 적합합니다.</p></div>
  <div class="feature-card"><p class="fc-num">04</p><h3>대면형</h3><p>거실을 바라보는 배치. 가족과 소통이 좋아 최근 선호도가 높습니다.</p></div>
</div>
<h2>자재별 선택 포인트</h2>
<ul class="spec-list">
  <li><b>상판</b> — 인조대리석(가성비)·세라믹(내열/내스크래치)·스테인리스(업소용)</li>
  <li><b>도어</b> — PET·무광 도장·필름. 오염·습기에 강한 마감 선택이 중요</li>
  <li><b>싱크볼</b> — 언더볼(청소 편의)·상부볼, 사이즈와 배수 위치</li>
  <li><b>타일</b> — 벽 타일·바닥 논슬립. 후드 뒤 유분 청소 편의 고려</li>
  <li><b>후드·전기</b> — 배기 성능, 인덕션 전용 배선(단독 회로) 확인</li>
</ul>
<h2>부분 교체 vs 전체 리모델링</h2>
<p>싱크대만 노후된 경우 <strong>상하부장·상판 교체</strong>만으로 충분할 때가 많습니다. 반면 배관 위치를 옮기거나 타일·바닥까지 바꾸면 전체 리모델링으로 넘어가며, 이때는 <a class="inline" href="/cheonan-bathroom-interior">욕실 공사</a>와 묶으면 효율이 좋습니다.</p>
""",
    faq=[
      ("천안 주방 싱크대 교체 비용은 얼마인가요?","길이와 자재에 따라 다르지만 상하부장·상판 교체 중심이면 약 150~400만 원 선입니다. 세라믹 상판·고급 도어를 쓰면 올라갑니다. 정확한 금액은 실측 후 산정됩니다."),
      ("주방 공사는 며칠 걸리나요?","싱크대 교체 중심은 1~2일, 타일·바닥·전기까지 포함한 전체 리모델링은 3~5일가량 소요됩니다."),
      ("타일 위에 덧방(덧시공)이 가능한가요?","기존 타일 상태가 양호하면 덧방이 가능해 철거 비용을 아낄 수 있습니다. 다만 들뜸·크랙이 있으면 철거 후 재시공을 권합니다."),
      ("인덕션으로 바꾸려면 전기 공사가 필요한가요?","인덕션은 전용 단독 회로가 필요한 경우가 많아, 분전반 여유와 배선 상태 점검이 함께 진행됩니다."),
    ],
    related=["cheonan-bathroom-interior","cheonan-apart-interior","cheonan-interior-cost"],
))

# 4) 욕실
PAGES.append(dict(
    slug="cheonan-bathroom-interior", label="Bathroom · 천안",
    h1="천안 욕실 인테리어",
    title="천안 욕실 인테리어 - 천안 욕실 리모델링·타일·방수·도기교체",
    desc="천안 욕실 인테리어 전문 정보. 방수·타일·도기(변기·세면대·수전) 교체, 건식/습식 구성, 노후 욕실 리모델링 절차와 방수 하자 주의점, 평당·개소별 비용 기준을 안내합니다.",
    keywords="천안욕실인테리어,천안욕실리모델링,천안화장실인테리어,천안욕실타일,천안욕실방수,천안변기교체,천안세면대교체",
    hero=unsplash("1600566752355-35792bedcfea"), hero_alt="천안 욕실 인테리어 시공 사례 - 모던 욕실 리모델링",
    serviceType=["욕실인테리어","욕실리모델링","타일시공","방수공사","도기교체"],
    aeo="<strong>천안 욕실 인테리어</strong>는 타일·도기(변기·세면대·수전)·방수·조명을 교체하는 리모델링으로, 방수가 가장 중요한 공정입니다. 표준 욕실 1개소 기준 <strong>200~500만 원</strong> 선이며, 철거 범위·타일 등급·건식 구성 여부에 따라 달라집니다. 공사는 보통 3~5일 소요됩니다.",
    body="""
<h2>욕실 리모델링 시공 범위</h2>
<ul class="spec-list">
  <li><b>철거</b> — 기존 타일·도기 철거(또는 상태 양호 시 덧방)</li>
  <li><b>방수</b> — 바닥·벽 방수층 시공. 하자의 90%가 방수에서 나오므로 핵심 공정</li>
  <li><b>타일</b> — 벽·바닥 타일, 논슬립·줄눈 마감</li>
  <li><b>도기·수전</b> — 변기·세면대·수전·샤워부스 교체</li>
  <li><b>조명·환기</b> — 방습등·환풍기, 젠다이·수납장</li>
</ul>
<h2>건식 vs 습식</h2>
<div class="feature-grid">
  <div class="feature-card"><p class="fc-num">01</p><h3>습식 욕실</h3><p>전통적 구성. 바닥 전체가 물 사용 구역으로, 배수와 방수가 관건입니다.</p></div>
  <div class="feature-card"><p class="fc-num">02</p><h3>건식·부분건식</h3><p>샤워부스로 물 구역을 분리. 세면·화장 공간이 마른 상태로 유지돼 관리가 편합니다.</p></div>
</div>
<h2>방수 하자 주의점</h2>
<p>욕실 공사에서 가장 흔한 문제는 <strong>아랫집 누수</strong>입니다. 방수층을 제대로 올리지 않거나 양생 시간을 지키지 않으면 몇 달 뒤 하자가 나타납니다. 방수 후 <strong>담수 테스트(물을 채워 누수 확인)</strong>를 거치는지 확인하는 것이 안전합니다. 노후 아파트는 <a class="inline" href="/cheonan-remodeling">배관 노후</a>까지 함께 점검하는 것이 좋습니다.</p>
""",
    faq=[
      ("천안 욕실 리모델링 비용은 얼마인가요?","표준 욕실 1개소 전체 리모델링은 약 200~500만 원 선입니다. 타일 등급, 도기 브랜드, 건식 구성(샤워부스) 여부에 따라 달라집니다."),
      ("욕실 공사는 며칠 걸리나요?","보통 3~5일입니다. 방수 양생 시간이 포함돼 무리하게 단축하지 않는 것이 하자 예방에 좋습니다."),
      ("타일 덧방을 하면 안 되나요?","기존 타일이 단단히 붙어 있으면 덧방이 가능합니다. 다만 들뜸·크랙·누수 이력이 있으면 철거 후 방수부터 다시 하는 것이 안전합니다."),
      ("공사 중 화장실을 못 쓰나요?","네, 공사 기간에는 사용이 어렵습니다. 화장실이 하나뿐이면 일정을 짧게 잡거나 대체 방안을 미리 협의합니다."),
    ],
    related=["cheonan-kitchen-interior","cheonan-remodeling","cheonan-interior-cost"],
))

# 5) 리모델링
PAGES.append(dict(
    slug="cheonan-remodeling", label="Remodeling · 천안",
    h1="천안 리모델링·집수리",
    title="천안 리모델링 - 천안 집수리·부분시공·노후주택 개선",
    desc="천안 리모델링·집수리 전문 정보. 도배·장판·샷시·문·조명 부분 시공부터 노후주택 전체 개선까지, 집수리와 전체 리모델링의 차이, 항목별 비용 기준과 진행 방법을 안내합니다.",
    keywords="천안리모델링,천안집수리,천안부분인테리어,천안도배,천안장판,천안샷시,천안문교체,천안조명공사,천안노후주택리모델링",
    hero=unsplash("1503387762-592deb58ef4e"), hero_alt="천안 리모델링 시공 사례 - 노후 주택 개선",
    serviceType=["리모델링","집수리","도배","장판","샷시","조명공사"],
    aeo="<strong>천안 리모델링·집수리</strong>는 도배·장판·조명 같은 부분 시공부터 배관·전기·구조까지 손보는 전체 리모델링을 포괄합니다. 부분 집수리는 <strong>수십만~수백만 원</strong>, 노후주택 전체 리모델링은 <strong>평당 90만 원 이상</strong>이 일반적이며, 어디까지 고칠지에 따라 예산이 크게 달라집니다.",
    body="""
<h2>집수리 vs 전체 리모델링</h2>
<p>"리모델링"과 "집수리"는 자주 섞여 쓰이지만 예산 규모가 다릅니다.</p>
<div class="feature-grid">
  <div class="feature-card"><p class="fc-num">01</p><h3>부분 집수리</h3><p>도배·장판·조명·문 교체 등 한두 가지만. 빠르고 저렴하게 분위기를 바꿉니다.</p></div>
  <div class="feature-card"><p class="fc-num">02</p><h3>전체 리모델링</h3><p>주방·욕실·샷시·전기·배관까지. 노후주택을 새집 수준으로 되돌립니다.</p></div>
</div>
<h2>부분 시공 메뉴</h2>
<ul class="spec-list">
  <li><b>도배·장판</b> — 가장 빠르고 효과 큰 분위기 전환</li>
  <li><b>샷시 교체</b> — 단열·결로·소음 개선(겨울철 체감 큼)</li>
  <li><b>문·몰딩</b> — 현관·방문 교체, 몰딩 정리로 완성도 향상</li>
  <li><b>조명·전기</b> — 매입등·스위치·콘센트 정비</li>
  <li><b>도장</b> — 발코니·천장 페인트로 곰팡이·오염 개선</li>
</ul>
<h2>노후주택 리모델링 시 점검</h2>
<p>준공 20년 이상 주택은 겉보다 <strong>속(배관·전기)</strong>이 문제인 경우가 많습니다. 누수·녹물·차단기 용량 부족은 마감을 다시 하기 전에 반드시 확인해야 합니다. <a class="inline" href="/cheonan-bathroom-interior">욕실</a>·<a class="inline" href="/cheonan-kitchen-interior">주방</a>을 함께 손보면 배관 공사를 한 번에 끝낼 수 있어 효율적입니다.</p>
""",
    faq=[
      ("도배·장판만 따로 해도 되나요?","네. 가장 수요가 많은 부분 시공입니다. 집 상태와 평형에 따라 하루~이틀이면 마무리됩니다."),
      ("노후주택 전체 리모델링 비용은?","범위에 따라 크게 달라지지만 배관·전기·주방·욕실까지 포함하면 평당 90만 원 이상에서 형성됩니다. 실측 견적이 필요합니다."),
      ("전세·월세 집도 수리가 되나요?","도배·조명 같은 부분 시공은 가능하나, 구조·배관 변경은 집주인 동의가 필요합니다. 원상복구 조건도 미리 확인하세요."),
      ("겨울에도 공사가 가능한가요?","가능합니다. 다만 도장·방수처럼 양생이 필요한 공정은 기온에 따라 건조 시간이 늘 수 있어 일정에 여유를 둡니다."),
    ],
    related=["cheonan-apart-interior","cheonan-bathroom-interior","cheonan-interior-cost"],
))

# 6) 비용
PAGES.append(dict(
    slug="cheonan-interior-cost", label="Cost Guide · 천안",
    h1="천안 인테리어 비용",
    title="천안 인테리어 비용 - 천안 인테리어 평당 단가·견적 기준",
    desc="천안 인테리어 비용 종합 가이드. 아파트·상업·사무실·주방·욕실 분야별 평당 단가, 견적을 구성하는 요소, 추가 비용이 생기는 지점과 비용을 아끼는 방법을 정리했습니다.",
    keywords="천안인테리어비용,천안인테리어견적,천안인테리어평당단가,천안아파트인테리어비용,천안리모델링비용,천안주방인테리어비용,천안욕실인테리어비용",
    hero=unsplash("1600585154340-be6161a56a0c"), hero_alt="천안 인테리어 비용 견적 - 시공 현장",
    serviceType=["인테리어견적","인테리어비용상담"],
    aeo="<strong>천안 인테리어 비용</strong>은 <strong>평수 × 시공 범위 × 자재 등급</strong>으로 결정됩니다. 부분 시공은 평당 40~70만 원, 아파트 올수리는 평당 90~150만 원, 상업 공간은 평당 100~200만 원 선이 일반적입니다. 정확한 금액은 현장 실측 후 항목별 견적으로 확인해야 합니다.",
    body="""
<h2>분야별 평당 참고 단가</h2>
<table class="cost-table">
  <thead><tr><th>분야</th><th>시공 범위</th><th>평당 참고가</th></tr></thead>
  <tbody>
    <tr><td>부분 인테리어</td><td>도배·바닥·조명 위주</td><td>40~70만 원</td></tr>
    <tr><td>아파트 올수리</td><td>주방·욕실·샷시·확장 포함</td><td>90~150만 원</td></tr>
    <tr><td>사무실 인테리어</td><td>파티션·전기·마감</td><td>60~120만 원</td></tr>
    <tr><td>상업 공간</td><td>카페·식당·상가 등</td><td>100~200만 원</td></tr>
  </tbody>
</table>
<h2>견적을 구성하는 요소</h2>
<ul class="spec-list">
  <li><b>철거·폐기물</b> — 범위가 클수록 처리 비용 증가</li>
  <li><b>자재 등급</b> — 같은 항목도 등급에 따라 배 이상 차이</li>
  <li><b>설비(전기·배관)</b> — 위치 변경 시 비용 크게 상승</li>
  <li><b>공정 수</b> — 주방·욕실·샷시를 함께 하면 인건비 효율↑</li>
  <li><b>현장 조건</b> — 엘리베이터 유무, 층수, 주차 등</li>
</ul>
<h2>추가 비용이 생기는 지점</h2>
<p>가장 흔한 추가 비용은 <strong>철거 후 발견되는 하자</strong>입니다. 노후 배관 누수, 곰팡이, 단열 문제 등은 뜯어봐야 보입니다. 견적서에 <strong>추가 발생 항목의 처리 기준</strong>이 명시돼 있는지 확인하면 분쟁을 줄일 수 있습니다.</p>
<h2>비용을 아끼는 방법</h2>
<ul class="spec-list">
  <li><b>덧방·부분 시공 활용</b> — 상태 양호 시 철거 최소화</li>
  <li><b>공정 묶기</b> — 주방·욕실 동시 진행으로 인건비 절감</li>
  <li><b>자재 선택 집중</b> — 눈에 띄는 곳에 예산, 나머지는 표준 등급</li>
  <li><b>성수기 회피</b> — 이사철 집중 시기를 피하면 일정·단가 유리</li>
</ul>
<div class="callout">※ 위 단가는 천안 지역 일반 기준을 정리한 참고 정보이며, 실제 견적은 현장 실측과 자재 선택에 따라 달라집니다.</div>
""",
    faq=[
      ("천안 인테리어 견적은 어떻게 받나요?","현장 실측 후 항목별 견적서를 받는 것이 정확합니다. 평수·시공 범위·자재 등급을 정한 뒤 비교하면 좋습니다."),
      ("견적서에서 꼭 확인할 항목은?","항목별 단가·자재 사양·공사 범위·추가 비용 처리 기준·A/S 조건입니다. '일식(한 덩어리)' 견적보다 항목이 나뉜 견적이 투명합니다."),
      ("평당 단가만으로 비교해도 되나요?","참고는 되지만 자재 등급과 포함 범위가 다르면 평당가만으로는 비교가 어렵습니다. 같은 조건으로 맞춰 비교해야 합니다."),
      ("계약금·잔금은 어떻게 나누나요?","보통 계약·중도·잔금으로 나눕니다. 공정 진행률에 맞춰 지급하고, 잔금은 하자 점검 후 지급하는 것이 안전합니다."),
    ],
    related=["cheonan-apart-interior","cheonan-office-interior","cheonan-interior-portfolio"],
))

# 7) 시공사례
PAGES.append(dict(
    slug="cheonan-interior-portfolio", label="Portfolio · 천안",
    h1="천안 인테리어 시공 사례",
    title="천안 인테리어 시공 사례 - 천안 아파트·상업·사무실 포트폴리오",
    desc="천안 인테리어 시공 사례 모음. 천안 아파트 리모델링, 카페·식당 상업 인테리어, 사무실·오피스 인테리어 등 분야별 포트폴리오를 통해 스타일과 완성도를 확인하세요.",
    keywords="천안인테리어시공사례,천안인테리어포트폴리오,천안아파트인테리어사례,천안카페인테리어사례,천안사무실인테리어사례,천안리모델링사례",
    hero=unsplash("1600210492486-724fe5c67fb0"), hero_alt="천안 인테리어 시공 사례 - 포트폴리오 대표 이미지",
    serviceType=["인테리어시공사례","포트폴리오"],
    aeo="<strong>천안 인테리어 시공 사례</strong>는 아파트 리모델링, 카페·식당 상업 인테리어, 사무실 인테리어 등 분야별로 나눠 확인할 수 있습니다. 사례를 볼 때는 마감 완성도, 동선 설계, 실제 사용 편의를 함께 살펴보는 것이 좋습니다.",
    body="""
<h2>주거 인테리어 사례</h2>
<div class="gallery">
  <figure><img src="%(g1)s" alt="천안 아파트 거실 리모델링 사례" loading="lazy"><figcaption>아파트 거실 리모델링</figcaption></figure>
  <figure><img src="%(g2)s" alt="천안 주방 인테리어 사례" loading="lazy"><figcaption>주방 리모델링</figcaption></figure>
  <figure><img src="%(g3)s" alt="천안 욕실 인테리어 사례" loading="lazy"><figcaption>욕실 리모델링</figcaption></figure>
</div>
<h2>상업 인테리어 사례</h2>
<div class="gallery">
  <figure><img src="%(g4)s" alt="천안 카페 인테리어 사례" loading="lazy"><figcaption>카페 인테리어</figcaption></figure>
  <figure><img src="%(g5)s" alt="천안 식당 인테리어 사례" loading="lazy"><figcaption>식당 리뉴얼</figcaption></figure>
  <figure><img src="%(g6)s" alt="천안 상가 인테리어 사례" loading="lazy"><figcaption>상가 인테리어</figcaption></figure>
</div>
<h2>사무실 인테리어 사례</h2>
<div class="gallery">
  <figure><img src="%(g7)s" alt="천안 사무실 인테리어 사례" loading="lazy"><figcaption>오피스 인테리어</figcaption></figure>
  <figure><img src="%(g8)s" alt="천안 공유오피스 인테리어 사례" loading="lazy"><figcaption>공유오피스</figcaption></figure>
  <figure><img src="%(g9)s" alt="천안 학원 인테리어 사례" loading="lazy"><figcaption>학원·교육 공간</figcaption></figure>
</div>
<div class="callout">※ 현재 이미지는 예시입니다. 입점 업체의 실제 시공 사진으로 교체하면 신뢰도와 전환율이 크게 올라갑니다.</div>
""" % dict(
        g1=unsplash("1600607687939-ce8a6c25118c",800), g2=unsplash("1556909114-f6e7ad7d3136",800),
        g3=unsplash("1600566752355-35792bedcfea",800), g4=unsplash("1554118811-1e0d58224f24",800),
        g5=unsplash("1555396273-367ea4eb4db5",800), g6=unsplash("1517248135467-4c7edcad34c4",800),
        g7=unsplash("1497366811353-6870744d04b2",800), g8=unsplash("1524758631624-e2822e304c36",800),
        g9=unsplash("1503676260728-1c00da094a0b",800),
    ),
    faq=[
      ("시공 사례 사진은 실제인가요?","현재 페이지는 예시 이미지로 구성돼 있으며, 입점 업체 등록 시 해당 업체의 실제 시공 사진으로 교체됩니다."),
      ("우리 집과 비슷한 사례를 볼 수 있나요?","평형·공간·예산이 비슷한 사례를 요청하면 참고용으로 안내받을 수 있습니다. 상담 시 조건을 알려주세요."),
      ("사례처럼 똑같이 시공되나요?","현장 구조와 예산에 따라 조정됩니다. 사례는 스타일과 완성도를 가늠하는 참고 자료로 활용하세요."),
    ],
    related=["cheonan-apart-interior","cheonan-office-interior","cheonan-interior-cost"],
))

# 8) FAQ (AEO 허브)
PAGES.append(dict(
    slug="cheonan-interior-faq", label="FAQ · 천안",
    h1="천안 인테리어 자주 묻는 질문",
    title="천안 인테리어 FAQ - 비용·기간·A/S·계약 자주 묻는 질문",
    desc="천안 인테리어 자주 묻는 질문 모음. 비용과 견적, 공사 기간, 계약과 대금, 하자·A/S, 자재 선택 등 천안에서 인테리어를 준비할 때 꼭 알아야 할 내용을 정리했습니다.",
    keywords="천안인테리어FAQ,천안인테리어질문,천안인테리어견적방법,천안인테리어AS,천안인테리어계약,천안인테리어하자,천안인테리어기간",
    hero=unsplash("1600585152220-90363fe7e115"), hero_alt="천안 인테리어 상담 - 자주 묻는 질문",
    serviceType=["인테리어상담"],
    aeo="이 페이지는 <strong>천안 인테리어</strong>를 준비할 때 가장 많이 묻는 질문을 비용·기간·계약·하자·자재로 나눠 정리한 것입니다. 대부분의 궁금증은 <strong>현장 실측 후 항목별 견적</strong>으로 명확해지며, 계약 전 A/S 조건과 추가 비용 기준을 확인하는 것이 중요합니다.",
    body="""
<h2>인테리어 준비, 이것부터 정하세요</h2>
<ul class="spec-list">
  <li><b>범위</b> — 부분 시공인지 전체 리모델링인지</li>
  <li><b>예산</b> — 총액과 우선순위(주방/욕실/거실 등)</li>
  <li><b>일정</b> — 입주일·이사일 기준 역산</li>
  <li><b>거주 여부</b> — 살면서 할지, 빈 집에서 할지</li>
</ul>
<p>아래 자주 묻는 질문에서 비용·기간·계약·하자 관련 내용을 확인하세요. 분야별 상세는 <a class="inline" href="/cheonan-interior-cost">비용 페이지</a>와 각 시공 페이지에서 볼 수 있습니다.</p>
""",
    faq=[
      ("천안 인테리어 비용은 어떻게 정해지나요?","평수 × 시공 범위 × 자재 등급으로 결정됩니다. 부분 시공은 평당 40~70만 원, 아파트 올수리는 90~150만 원, 상업 공간은 100~200만 원 선이 일반적입니다."),
      ("견적은 무료인가요?","대부분 현장 실측·견적은 무료로 진행됩니다. 다만 상세 도면·3D 설계가 포함되면 별도 비용이 있을 수 있어 미리 확인하세요."),
      ("공사 기간은 보통 얼마나 걸리나요?","부분 시공은 1~5일, 욕실 1개소는 3~5일, 아파트 전체 올수리는 2~4주가량입니다. 범위와 평형에 따라 달라집니다."),
      ("계약금과 잔금은 어떻게 나누나요?","보통 계약·중도·잔금으로 나눠 공정 진행률에 맞춰 지급합니다. 잔금은 하자 점검 후 지급하는 것이 안전합니다."),
      ("하자가 생기면 A/S가 되나요?","계약서에 A/S 기간과 범위를 명시하는 것이 중요합니다. 방수·누수 등 중요한 하자는 기간을 넉넉히 잡는 것이 좋습니다."),
      ("살면서 공사할 수 있나요?","도배·조명·부분 시공은 거주 중에도 가능합니다. 전체 올수리는 빈 집 상태가 효율적이고 안전합니다."),
      ("자재는 직접 고를 수 있나요?","네. 타일·상판·바닥재 등은 샘플을 보고 선택합니다. 예산에 맞춰 등급을 조정할 수 있습니다."),
      ("천안 어느 지역까지 시공하나요?","천안 서북구·동남구 전역과 인접한 아산시까지 상담·시공이 가능합니다."),
    ],
    related=["cheonan-interior-cost","cheonan-apart-interior","cheonan-remodeling"],
))

# ─────────────────────────────────────────────
# 렌더링
# ─────────────────────────────────────────────
PAGE_BY_SLUG = {p["slug"]: p for p in PAGES}

def jsonld_localbusiness(p):
    return {
        "@context":"https://schema.org","@type":"LocalBusiness","name":CONFIG["biz"],
        "url":f'{D}/{p["slug"]}',"description":p["desc"],"image":CONFIG["og_image"],
        "telephone":CONFIG["phone_intl"],
        "address":{"@type":"PostalAddress","addressLocality":"천안시","addressRegion":"충청남도","addressCountry":"KR"},
        "areaServed":[{"@type":"City","name":"천안시"},{"@type":"City","name":"아산시"}],
        "serviceType":p["serviceType"],
    }

def jsonld_breadcrumb(p):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":CONFIG["biz"],"item":f'{D}/'},
        {"@type":"ListItem","position":2,"name":p["h1"],"item":f'{D}/{p["slug"]}'},
    ]}

def jsonld_webpage(p):
    return {"@context":"https://schema.org","@type":"WebPage","name":p["h1"],
        "url":f'{D}/{p["slug"]}',"inLanguage":"ko",
        "speakable":{"@type":"SpeakableSpecification","cssSelector":[".aeo-answer",".page-h1"]}}

def jsonld_faq(p):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]
    ]}

def faq_html(p):
    items=[]
    for q,a in p["faq"]:
        items.append(
            '<div class="faq-item"><button class="faq-q">'+q+'<span class="ico">+</span></button>'
            '<div class="faq-a"><div class="faq-a-inner">'+a+'</div></div></div>')
    return "\n".join(items)

def related_html(p):
    cards=[]
    for slug in p["related"]:
        rp=PAGE_BY_SLUG[slug]
        cat=rp["label"].split("·")[0].strip()
        cards.append(
            f'<a href="/{rp["slug"]}" class="related-card"><p class="rc-cat">{cat}</p>'
            f'<p class="rc-title">{rp["h1"]}</p><p class="rc-desc">{rp["desc"][:34]}…</p></a>')
    return "\n".join(cards)

def footer_html():
    cols=[]
    for heading, links in FOOTER_COLS:
        ls="\n".join(f'<a href="{u}">{t}</a>' for u,t in links)
        cols.append(f'<div><h4 class="footer-heading">{heading}</h4><div class="footer-links">{ls}</div></div>')
    return "\n".join(cols)

def render(p):
    ld = "\n".join(
        '<script type="application/ld+json">'+json.dumps(x, ensure_ascii=False)+'</script>'
        for x in [jsonld_localbusiness(p), jsonld_breadcrumb(p), jsonld_webpage(p), jsonld_faq(p)])
    url=f'{D}/{p["slug"]}'
    html=f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="robots" content="index,follow">
<meta name="NaverBot" content="index,follow">
<meta name="Yeti" content="index,follow">
<meta name="Googlebot" content="index,follow">
<meta name="format-detection" content="telephone=no">
<meta name="description" content="{p['desc']}">
<meta name="keywords" content="{p['keywords']}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{CONFIG['og_image']}">
<meta property="og:site_name" content="{CONFIG['biz']}">
<meta property="og:locale" content="ko_KR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p['h1']}">
<meta name="twitter:description" content="{p['desc']}">
<meta name="twitter:image" content="{CONFIG['og_image']}">
<title>{p['title']}</title>
<link rel="stylesheet" href="/subpage.css">
{ld}
</head>
<body>
<header class="header" id="header">
  <div class="header-inner">
    <a href="/" class="logo">천안<span>인테리어</span></a>
    <nav><ul class="nav-links" id="navLinks">
      <li><a href="/#services">서비스 안내</a></li>
      <li><a href="/#portfolio">시공 사례</a></li>
      <li><a href="/#guide">비용 가이드</a></li>
      <li><a href="/#reviews">고객 후기</a></li>
      <li><a href="{CONFIG['ad_link']}" class="nav-cta">광고 입점 문의</a></li>
    </ul></nav>
    <button class="menu-toggle" id="menuToggle" aria-label="메뉴 열기"><span></span><span></span><span></span></button>
  </div>
</header>

<section class="page-hero"><div class="container">
  <nav class="breadcrumb" aria-label="breadcrumb"><a href="/">천안인테리어</a><span>›</span><span>{p['h1']}</span></nav>
  <p class="page-label">{p['label']}</p>
  <h1 class="page-h1">{p['h1']}</h1>
  <p class="aeo-answer">{p['aeo']}</p>
</div></section>

<article class="article"><div class="container">
  <div class="article-hero-img"><img src="{p['hero']}" alt="{p['hero_alt']}" loading="lazy"></div>
  {p['body']}
</div></article>

<section class="faq"><div class="container">
  <div class="faq-head"><p class="page-label" style="text-align:center;">FAQ</p>
  <h2 style="font-family:var(--font-display);font-size:clamp(1.6rem,3vw,2.2rem);font-weight:700;color:var(--c-dark);">{p['h1'].replace('천안 ','천안 ')} 자주 묻는 질문</h2></div>
  {faq_html(p)}
</div></section>

<section class="related"><div class="container">
  <div class="related-head"><p class="related-label">함께 보면 좋은 페이지</p>
  <h2 class="related-title">천안 인테리어 다른 정보도 확인하세요</h2></div>
  <div class="related-grid">{related_html(p)}</div>
</div></section>

<section class="cta"><div class="container">
  <h2 class="cta-title">{p['h1']} 업체 사장님, 이 자리에 노출되세요</h2>
  <p class="cta-desc">천안 지역 인테리어 전문 업체라면 광고 입점으로 고객에게 직접 노출됩니다.</p>
  <a href="{CONFIG['ad_link']}" class="btn btn-dark">광고 입점 문의</a>
</div></section>

<footer class="footer"><div class="container">
  <div class="footer-grid">
    <div><div class="footer-logo">천안<span>인테리어</span></div>
      <p class="footer-desc">천안인테리어, 천안아파트인테리어, 천안리모델링,<br>천안도배, 천안욕실인테리어, 천안주방인테리어 등<br>천안 지역 인테리어 정보를 제공합니다.<br><br>천안 인테리어 업체 광고 입점 문의 환영합니다.</p></div>
    {footer_html()}
    <div><h4 class="footer-heading">광고 문의</h4><div class="footer-links">
      <a href="tel:{CONFIG['phone']}">&#9742; {CONFIG['phone']}</a>
      <a href="{CONFIG['ad_link']}">입점 신청하기</a></div></div>
  </div>
  <div class="footer-bottom"><p>COPYRIGHT &copy; 2026 천안인테리어. ALL RIGHTS RESERVED.</p>
    <div><a href="{CONFIG['ad_link']}">광고 입점 문의</a></div></div>
</div></footer>

<div class="floating-cta">
  <a href="tel:{CONFIG['phone']}" class="float-btn float-btn-phone" aria-label="전화 문의">&#9742;</a>
  <button class="float-btn float-btn-top" id="btnTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" aria-label="상단으로">&#9650;</button>
</div>

<script>
document.addEventListener('DOMContentLoaded',function(){{
  var header=document.getElementById('header');
  window.addEventListener('scroll',function(){{
    if(window.scrollY>50)header.classList.add('scrolled');else header.classList.remove('scrolled');
    var t=document.getElementById('btnTop');
    if(t){{if(window.scrollY>600)t.classList.add('visible');else t.classList.remove('visible');}}
  }});
  var mt=document.getElementById('menuToggle'),nl=document.getElementById('navLinks');
  if(mt&&nl){{mt.addEventListener('click',function(){{mt.classList.toggle('active');nl.classList.toggle('open');}});
    nl.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',function(){{mt.classList.remove('active');nl.classList.remove('open');}});}});}}
  document.querySelectorAll('.faq-q').forEach(function(btn){{
    btn.addEventListener('click',function(){{
      var item=btn.closest('.faq-item'),ans=item.querySelector('.faq-a'),isOpen=item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function(o){{o.classList.remove('open');o.querySelector('.faq-a').style.maxHeight=null;}});
      if(!isOpen){{item.classList.add('open');ans.style.maxHeight=ans.scrollHeight+'px';}}
    }});
  }});
}});
</script>
</body>
</html>"""
    return html

# 파일 출력
for p in PAGES:
    with open(os.path.join(OUT, p["slug"]+".html"), "w", encoding="utf-8") as f:
        f.write(render(p))

# sitemap.xml (메인 + 서브 8장)
import datetime
LASTMOD = datetime.date.today().isoformat()   # 배포일 기준
urls = [f'{D}/'] + [f'{D}/{p["slug"]}' for p in PAGES]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    pr = "1.0" if u.endswith("/") else "0.8"
    sm.append(f'  <url>\n    <loc>{u}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{pr}</priority>\n  </url>')
sm.append('</urlset>')
open(os.path.join(OUT,"sitemap.xml"),"w",encoding="utf-8").write("\n".join(sm))

# robots.txt
robots = f"""User-agent: *
Allow: /

User-agent: Yeti
Allow: /

User-agent: Googlebot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {D}/sitemap.xml
"""
open(os.path.join(OUT,"robots.txt"),"w",encoding="utf-8").write(robots)

# rss.xml (네이버용)
items=[]
for p in PAGES:
    items.append(f"""  <item>
    <title>{p['h1']}</title>
    <link>{D}/{p['slug']}</link>
    <description>{p['desc']}</description>
    <guid>{D}/{p['slug']}</guid>
  </item>""")
rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>천안인테리어</title>
  <link>{D}/</link>
  <description>천안 지역 인테리어 정보 - 아파트·상업·사무실 인테리어, 리모델링, 주방·욕실 시공 안내</description>
  <language>ko</language>
{chr(10).join(items)}
</channel>
</rss>"""
open(os.path.join(OUT,"rss.xml"),"w",encoding="utf-8").write(rss)

print("생성 완료:", len(PAGES), "페이지 + sitemap/robots/rss")
for p in PAGES:
    print(" -", p["slug"]+".html")
