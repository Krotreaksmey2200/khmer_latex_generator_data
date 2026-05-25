import google.generativeai as genai
import logging

class KhmerMathGenerator:
    def __init__(self, api_key):
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-2.0-flash")
        except Exception as e:
            logging.error(f"Failed to configure Gemini: {e}")
            raise Exception(f"Failed to configure Gemini: {str(e)}")

    def generate(self, additional_context=""):
        context_str = f"\nSpecific focus for this request: {additional_context}" if additional_context else ""

        prompt = f"""
        Your task is to generate a diverse set of mathematical content in Khmer language mixed with LaTeX formulas.
        The output must be a single line of text.
        {context_str}

        General variations to include (unless specified otherwise in focus):
        1. Algebra: Equations, inequalities, factoring, functions.
        2. Calculus: Derivatives, integrals, limits, series.
        3. Geometry: Area, volume, trigonometry, properties of shapes.
        4. Arithmetic/Number Theory: Prime numbers, GCD, LCM, fractions.
        5. Statistics/Probability.
        6. Logical Word Problems.

        Requirements:
        1. Language: Use natural and correct Khmer mathematical terminology.
        2. LaTeX: All mathematical symbols, variables, and formulas MUST be enclosed in $ ... $.
        3. Format: Output ONLY the raw text line. DO NOT use markdown code blocks (```), bolding, or numbering.
        4. Realistic: The problems should look like they are from a Khmer textbook or exam.
        """
        try:
            response = self.model.generate_content(prompt)
            if response and response.text:
                text = response.text.strip().replace("```", "").replace("**", "")
                return text
            return "Error: Empty response from AI"
        except Exception as e:
            logging.error(f"Generation error: {e}")
            return f"Error: {str(e)}"
