# AI-Powered Investor Assistant Workflow

## Objective
Develop an AI model that takes structured startup data and investor preferences as input and provides a match score between founders and investors.

## Overview
This AI model aims to assist investors in identifying startups that best match their investment preferences. By considering various criteria such as industry, investment range, startup stage, and traction, the model will filter and rank startups, providing a match score (0-100) for each.

## Components

### 1. Structured Startup Data
The startup data will be stored in a structured format, such as a SQL database. This data will include:
- **Industry:** The sector or industry the startup operates in.
- **Funding Range:** The range of funding the startup has received.
- **Startup Stage:** The stage of the startup (e.g., seed, series A, series B).
- **Traction:** Metrics indicating the startup's traction, such as revenue, user growth, or market presence.

### 2. Investor Preferences
Investors will provide their preferences which may include:
- **Preferred Industry:** The industry they are interested in.
- **Investment Range:** The range of investment they are willing to make.
- **Preferred Startup Stage:** The stage of the startup they prefer to invest in.
- **Minimum Traction Requirement:** The minimum traction metrics they require.

### 3. AI Model
The AI model will process the startup data and investor preferences to generate a match score. The key tasks of the model include:
1. **Filter Startups:** Based on the investor's preferences.
2. **Calculate Match Score:** Determine how well each startup meets the investor's criteria, providing a score between 0 and 100.
3. **Rank Startups:** Rank the startups from highest to lowest match score.
4. **Provide Reasoning:** Offer an explanation for the ranking and match scores.

### 4. Implementation Steps

#### Data Preparation
- Collect and structure startup data in a database.
- Ensure the data includes all relevant fields (industry, funding, stage, traction).

#### Model Development
- Define the prompt template for the AI model.
- Implement the function to filter startups based on investor preferences.
- Develop the scoring mechanism to calculate match scores.

#### Integration
- Integrate the AI model with a chat interface (e.g., using Gradio) to enable user interaction.
- Ensure the model can process inputs and provide outputs in a structured format.

#### Testing and Validation
- Test the model with various investor preferences and startup data.
- Validate the accuracy and relevance of the match scores and rankings.

## Example Usage

### Pre-Launch Operations
1. Load startup data from a JSON file.
2. Create a SQLite database and store the startup data in it.
3. Initialize the AI model using ChatGoogleGenerativeAI.
4. Create a SQL agent with the AI model and the database.

### Chat Interface
1. Define a function that will handle the interaction with the user.
2. Launch the chat interface using Gradio.

### Conclusion
This AI model will help investors efficiently identify and evaluate startups that align with their investment criteria, streamlining the decision-making process and enhancing investment outcomes.
### Web App Link:[GitHub](https://huggingface.co/spaces/shahir123/vertext_1)
