---
layout: quiz
title: NYC Mayoral Quiz
---

<!-- Welcome Card -->
<div id="welcomeCard" class="w-full max-w-2xl bg-white rounded-xl shadow-lg overflow-hidden">
    <div class="bg-blue-600 py-3 px-6">
        <h1 class="text-white font-bold text-xl">NYC Mayoral Match Quiz</h1>
    </div>
    <div class="p-6 space-y-4">
        <div class="flex items-center space-x-4 mb-6">
            <div class="bg-blue-100 p-3 rounded-lg">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-blue-600" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </div>
            <div>
                <h2 class="font-semibold text-lg">Find Your Match</h2>
                <p class="text-slate-600">Discover which NYC mayoral candidate aligns with your views</p>
            </div>
        </div>

        <p class="text-slate-700">
            Welcome to the NYC Mayoral Match Quiz! This short quiz will help you see which mayoral candidate your views
            align with.
            Each statement can be answered with "agree," "disagree," or "skip."
        </p>

        <div class="bg-blue-50 p-4 rounded-lg border border-blue-100 flex items-start space-x-3 mt-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500 mt-0.5 flex-shrink-0" fill="none"
                viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p class="text-sm text-slate-600">
                The quiz contains 13 questions and takes about 3 minutes to complete. At the end, you'll see how your
                answers align with each mayoral candidate's platform.
            </p>
        </div>

        <div class="flex justify-end mt-4">
            <button id="startQuizBtn"
                class="px-6 py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors flex items-center">
                Start Quiz
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-1" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
            </button>
        </div>
    </div>
</div>

<!-- Quiz Container (hidden until Start) -->
<div id="quizContainer" class="w-full max-w-2xl hidden">
    <!-- Progress Bar -->
    <div class="w-full bg-gray-200 rounded-full h-2.5 mb-6">
        <div id="progressBar" class="bg-blue-600 h-2.5 rounded-full progress-bar" style="width: 0%"></div>
    </div>

    <!-- Each question is in its own "card" -->
    <!-- 1 -->
    <div data-question="1" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            1. New York City should increase the number of NYPD officers to crack down on crime and enforce
            quality-of-life offenses.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q1" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q1" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q1" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 2 -->
    <div data-question="2" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            2. We should freeze or strictly cap rents across the city to provide immediate relief for tenants.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q2" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q2" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q2" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 3 -->
    <div data-question="3" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            3. We should rely less on policing and invest more in mental health services, violence interruption, and
            social programs to address crime.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q3" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q3" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q3" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 4 -->
    <div data-question="4" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            4. Free childcare should be provided for all families in New York City, just like we provide free public
            education.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q4" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q4" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q4" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 5 -->
    <div data-question="5" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            5. To tackle the migrant crisis, the city must prioritize local residents for resources over new arrivals.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q5" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q5" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q5" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 6 -->
    <div data-question="6" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            6. A major housing goal (like building or preserving one million units) is essential to solve NYC's
            affordability crisis, even if it means upzoning more neighborhoods.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q6" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q6" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q6" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 7 -->
    <div data-question="7" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            7. The mayor should aggressively expand the number of charter schools and give families more school-choice
            options.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q7" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q7" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q7" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 8 -->
    <div data-question="8" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            8. We should make public buses in NYC free for everyone, funded by new taxes or reallocating money from other
            parts of the budget.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q8" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q8" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q8" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 9 -->
    <div data-question="9" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            9. City government should be shrunk and its spending reined in to ease the tax burden on businesses and
            residents.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q9" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q9" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q9" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 10 -->
    <div data-question="10" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            10. Homeless New Yorkers with serious mental illness should be forced into treatment if they refuse help on
            the streets.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q10" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q10" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q10" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 11 -->
    <div data-question="11" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            11. We should legalize and convert more basement apartments, office buildings, and other spaces into housing
            as quickly as possible.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q11" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q11" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q11" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 12 -->
    <div data-question="12" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            12. Police reform and accountability—like stronger oversight and curbing abusive practices—should be a higher
            priority than hiring new officers.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q12" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q12" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q12" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 13 -->
    <div data-question="13" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            13. It's better to attract large businesses and major development projects (stadiums, casinos, corporate
            offices) than to risk them leaving NYC.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q13" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q13" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q13" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- 14 -->
    <div data-question="14" class="quiz-card hidden bg-white rounded-xl shadow-lg p-6 space-y-4">
        <p class="font-semibold text-lg mb-4">
            14. NYC must achieve ambitious climate goals by investing heavily in green jobs, renewable energy, and climate
            resilience infrastructure—whatever the cost.
        </p>
        <div class="space-y-3 mt-6">
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q14" value="agree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Agree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q14" value="disagree" class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Disagree</span>
            </label>
            <label
                class="flex items-center p-3 border border-gray-200 rounded-lg hover:bg-blue-50 transition-colors radio-button">
                <input type="radio" name="q14" value="skip" checked class="hidden" />
                <span class="checkmark"></span>
                <span class="ml-2">Skip</span>
            </label>
        </div>
    </div>

    <!-- Navigation/Actions -->
    <div class="mt-6 flex justify-between items-center">
        <button id="prevBtn"
            class="px-5 py-2.5 bg-white border border-gray-300 text-slate-600 rounded-lg hover:bg-gray-50 font-medium transition-colors hidden flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
            </svg>
            Previous
        </button>
        <button id="nextBtn"
            class="px-5 py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium transition-colors flex items-center">
            Next
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-1" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
        </button>
        <button id="scoreBtn"
            class="px-5 py-2.5 bg-green-600 text-white rounded-lg hover:bg-green-700 font-medium transition-colors hidden flex items-center">
            See Results
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-1" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 19l3 3 3-3m0 0V5m0 0L9 8m6-3l3 3" />
            </svg>
        </button>
    </div>
</div>

<!-- Results Card -->
<div id="resultsCard" class="w-full max-w-2xl bg-white rounded-xl shadow-lg overflow-hidden hidden">
    <div class="bg-green-600 py-3 px-6">
        <h2 class="text-white font-bold text-xl">Your Results</h2>
    </div>
    <div class="p-6">
        <div class="flex items-center space-x-3 mb-6">
            <div class="bg-green-100 p-2 rounded-lg">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-green-600" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </div>
            <p class="font-medium text-slate-800">Based on your answers, here's how you match with the candidates:</p>
        </div>

        <div id="scoreList" class="space-y-4"></div>

        <div class="mt-8 pt-6 border-t border-gray-200">
            <p class="text-sm text-slate-600 mb-4">Want to learn more about these candidates or take another quiz?</p>
            <div class="flex flex-wrap gap-3">
                <button onclick="window.location.reload()"
                    class="px-4 py-2 bg-blue-100 text-blue-600 rounded-lg hover:bg-blue-200 font-medium transition-colors text-sm">
                    Retake Quiz
                </button>
                <a href="/about/"
                    class="px-4 py-2 bg-slate-100 text-slate-600 rounded-lg hover:bg-slate-200 font-medium transition-colors text-sm">
                    Learn More About Candidates
                </a>
            </div>
        </div>
    </div>
</div>
