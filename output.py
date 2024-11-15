
qnr2_examples: List[BaseSystemPrompt | BaseExample] = [
    BaseSystemPrompt(system_prompt=chunk_part_extractor_system_prompt),
    Example(
        input=textwrap.dedent(
            """
1: <h1 style="margin-top:13.6pt; margin-left:29.75pt; margin-bottom:0pt; text-indent:-19.15pt; font-size:13.5pt" id="Q1">
2:   <span>
3:     <span style="color:#18186f">
4:       1.
5:     </span>
6:   </span>
7:   <span style="color:#18186f">
8:     Frequency
9:   </span>
10: </h1>
11: <p style="margin-top:12.35pt; margin-left:10.6pt; margin-bottom:0pt; font-size:9pt">
12:   <span>
13:     [Q1]
14:   </span>
15:   <span>
16:     How
17:   </span>
18:   <span>
19:     often
20:   </span>
21:   <span>
22:     do
23:   </span>
24:   <span>
25:     you
26:   </span>
27:   <span>
28:     visit
29:   </span>
30:   <span>
31:     our
32:   </span>
33:   <span>
34:     coffee
35:   </span>
36:   <span>
37:     shops?
38:   </span>
39: </p>
40: <p style="margin-top:9.95pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
41:   <span>
42:     <span>
43:       1.
44:     </span>
45:   </span>
46:   <span>
47:     Daily
48:   </span>
49: </p>
50: <p style="margin-top:0.7pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
51:   <span>
52:     <span>
53:       2.
54:     </span>
55:   </span>
56:   <span>
57:     Several
58:   </span>
59:   <span>
60:     times
61:   </span>
62:   <span>
63:     a
64:   </span>
65:   <span>
66:     week
67:   </span>
68: </p>
69: <p style="margin-top:0.75pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
70:   <span>
71:     <span>
72:       3.
73:     </span>
74:   </span>
75:   <span>
76:     Once
77:   </span>
78:   <span>
79:     a
80:   </span>
81:   <span>
82:     week
83:   </span>
84: </p>
85: <p style="margin-top:0.7pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
86:   <span>
87:     <span>
88:       4.
89:     </span>
90:   </span>
91:   <span>
92:     A
93:   </span>
94:   <span>
95:     few
96:   </span>
97:   <span>
98:     times
99:   </span>
100:   <span>
101:     a
102:   </span>
103:   <span>
104:     month
105:   </span>
106: </p>
107: <p style="margin-top:0.7pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
108:   <span>
109:     <span>
110:       5.
111:     </span>
112:   </span>
113:   <span>
114:     Less
115:   </span>
116:   <span>
117:     often
118:   </span>
119: </p>
120: <p style="margin-top:0.75pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
121:   <span>
122:     <span>
123:       6.
124:     </span>
125:   </span>
126:   <span>
127:     This
128:   </span>
129:   <span>
130:     is
131:   </span>
132:   <span>
133:     my
134:   </span>
135:   <span>
136:     first
137:   </span>
138:   <span>
139:     visit
140:   </span>
141: </p>
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),
    Example(
        input=textwrap.dedent(
            """
1: <p style="margin-top:9.9pt; margin-left:10.6pt; margin-bottom:0pt; font-size:9pt" id="device_type">
2:   <span style="font-size:7.5pt">
3:     [HIDDEN]
4:   </span>
5:   <span>
6:     device_type
7:   </span>
8:   <span>
9:     =
10:   </span>
11:   <span>
12:     GET_DEVICE_TYPE()
13:   </span>
14: </p>
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),
    Example(
        input=textwrap.dedent(
            """
1: <p style="margin:9.65pt 19.35pt 0pt 10.6pt; font-size:9pt" id="Q2">
2:   <span>
3:     [Q2]
4:   </span>
5:   <span>
6:     On
7:   </span>
8:   <span>
9:     a
10:   </span>
11:   <span>
12:     scale
13:   </span>
14:   <span>
15:     of
16:   </span>
17:   <span>
18:     1
19:   </span>
20:   <span>
21:     to
22:   </span>
23:   <span>
24:     10,
25:   </span>
26:   <span>
27:     how
28:   </span>
29:   <span>
30:     would
31:   </span>
32:   <span>
33:     you
34:   </span>
35:   <span>
36:     rate
37:   </span>
38:   <span>
39:     your
40:   </span>
41:   <span>
42:     overall
43:   </span>
44:   <span>
45:     experience
46:   </span>
47:   <span>
48:     at
49:   </span>
50:   <span>
51:     our
52:   </span>
53:   <span>
54:     coffee shop today? 1 (Very Poor) to 10 (Excellent)
55:   </span>
56: </p>
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),
    Example(
        input=textwrap.dedent(
            """
1: <p style="margin-top:9.25pt; margin-left:10.6pt; margin-bottom:0pt; font-size:9pt" id="Q3">
2:   <span>
3:     [Q3]
4:   </span>
5:   <span>
6:     What
7:   </span>
8:   <span>
9:     did
10:   </span>
11:   <span>
12:     you
13:   </span>
14:   <span>
15:     order
16:   </span>
17:   <span>
18:     today?
19:   </span>
20:   <span>
21:     (Select
22:   </span>
23:   <span>
24:     all
25:   </span>
26:   <span>
27:     that
28:   </span>
29:   <span>
30:     apply)
31:   </span>
32: </p>
33: <ol style="margin:0pt; padding-left:0pt" type="1">
34:   <li style="margin-top:9.95pt; margin-left:30.49pt; padding-left:3.01pt; font-size:9pt">
35:     <span>
36:       Coffee
37:     </span>
38:   </li>
39:   <li style="margin-top:0.7pt; margin-left:31.65pt; padding-left:1.85pt; font-size:9pt">
40:     <span>
41:       Tea
42:     </span>
43:   </li>
44:   <li style="margin-top:0.7pt; margin-left:31.59pt; padding-left:1.91pt; font-size:9pt">
45:     <span>
46:       Espresso-based
47:     </span>
48:     <span>
49:       drink
50:     </span>
51:     <span>
52:       (latte,
53:     </span>
54:     <span>
55:       cappuccino,
56:     </span>
57:     <span>
58:       etc.)
59:     </span>
60:   </li>
61:   <li style="margin-top:0.75pt; margin-left:31.71pt; padding-left:1.79pt; font-size:9pt">
62:     <span>
63:       Cold
64:     </span>
65:     <span>
66:       brew
67:     </span>
68:   </li>
69:   <li style="margin-top:0.7pt; margin-left:31.38pt; padding-left:2.12pt; font-size:9pt">
70:     <span>
71:       Pastry
72:     </span>
73:     <span>
74:       or
75:     </span>
76:     <span>
77:       snack
78:     </span>
79:   </li>
80:   <li style="margin-top:0.7pt; margin-left:31.72pt; padding-left:1.78pt; font-size:9pt">
81:     <span>
82:       Sandwich
83:     </span>
84:     <span>
85:       or
86:     </span>
87:     <span>
88:       meal
89:     </span>
90:   </li>
91: </ol>
92: <p style="margin-top:2.05pt; margin-bottom:0pt; font-size:9pt">
93: </p>
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),
    Example(
        input=textwrap.dedent(
            """
1: <h1 style="margin-top:0pt; margin-left:29.75pt; margin-bottom:0pt; text-indent:-19.15pt; font-size:13.5pt" id="Q4">
2:   <span>
3:     <span style="color:#18186f">
4:       2.
5:     </span>
6:   </span>
7:   <span style="color:#18186f">
8:     Feedback
9:   </span>
10: </h1>
11: <p style="margin:12.4pt 19.35pt 0pt 10.6pt; font-size:9pt">
12:   <span>
13:     [Q4]
14:   </span>
15:   <span>
16:     [ASK
17:   </span>
18:   <span>
19:     IF
20:   </span>
21:   <span>
22:     Q2
23:   </span>
24:   <span>
25:     &lt;
26:   </span>
27:   <span>
28:     7]
29:   </span>
30:   <span>
31:     We’re
32:   </span>
33:   <span>
34:     sorry
35:   </span>
36:   <span>
37:     to
38:   </span>
39:   <span>
40:     hear
41:   </span>
42:   <span>
43:     your
44:   </span>
45:   <span>
46:     experience
47:   </span>
48:   <span>
49:     wasn’t
50:   </span>
51:   <span>
52:     great.
53:   </span>
54:   <span>
55:     What
56:   </span>
57:   <span>
58:     areas do you think we could improve? (Select all that apply)
59:   </span>
60: </p>
61: <p style="margin-top:9.2pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
62:   <span>
63:     <span>
64:       1.
65:     </span>
66:   </span>
67:   <span>
68:     Coffee
69:   </span>
70:   <span>
71:     quality
72:   </span>
73: </p>
74: <p style="margin-top:0.7pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
75:   <span>
76:     <span>
77:       2.
78:     </span>
79:   </span>
80:   <span>
81:     Food
82:   </span>
83:   <span>
84:     quality
85:   </span>
86: </p>
87: <p style="margin-top:0.75pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
88:   <span>
89:     <span>
90:       3.
91:     </span>
92:   </span>
93:   <span>
94:     Service
95:   </span>
96:   <span>
97:     speed
98:   </span>
99: </p>
100: <p style="margin-top:0.7pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
101:   <span>
102:     <span>
103:       4.
104:     </span>
105:   </span>
106:   <span>
107:     Staff
108:   </span>
109:   <span>
110:     friendliness
111:   </span>
112: </p>
113: <p style="margin-top:0.7pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
114:   <span>
115:     <span>
116:       5.
117:     </span>
118:   </span>
119:   <span>
120:     Cleanliness
121:   </span>
122: </p>
123: <p style="margin-top:0.75pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
124:   <span>
125:     <span>
126:       6.
127:     </span>
128:   </span>
129:   <span>
130:     Atmosphere
131:   </span>
132: </p>
133: <p style="margin-top:0.7pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
134:   <span>
135:     <span>
136:       7.
137:     </span>
138:   </span>
139:   <span>
140:     Value
141:   </span>
142:   <span>
143:     for
144:   </span>
145:   <span>
146:     money
147:   </span>
148: </p>
149: <p style="margin-top:0.7pt; margin-left:33.5pt; margin-bottom:0pt; text-indent:-14.3pt; font-size:9pt">
150:   <span>
151:     <span>
152:       8.
153:     </span>
154:   </span>
155:   <span>
156:     Other
157:   </span>
158:   <span>
159:     (please
160:   </span>
161:   <span>
162:     specify):
163:   </span>
164:   <span>
165:     [TEXT]
166:   </span>
167: </p>
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),
    Example(
        input=textwrap.dedent(
            """
1: <p style="margin:9.95pt 19.35pt 0pt 10.6pt; font-size:9pt" id="Q5">
2:   <span>
3:     [Q5] [ASK IF Q2 &gt;= 7] We’re glad you had a good experience! What did you
4:   </span>
5:   <span>
6:     particularly enjoy about your visit? (Select all that apply)
7:   </span>
8: </p>
9: <ol style="margin:0pt; padding-left:0pt" type="1">
10:   <li style="margin-top:9.25pt; margin-left:30.49pt; padding-left:3.01pt; font-size:9pt">
11:     <span>
12:       Coffee
13:     </span>
14:     <span>
15:       quality
16:     </span>
17:   </li>
18:   <li style="margin-top:0.7pt; margin-left:31.65pt; padding-left:1.85pt; font-size:9pt">
19:     <span>
20:       Food
21:     </span>
22:     <span>
23:       quality
24:     </span>
25:   </li>
26:   <li style="margin-top:0.7pt; margin-left:31.59pt; padding-left:1.91pt; font-size:9pt">
27:     <span>
28:       Service
29:     </span>
30:     <span>
31:       speed
32:     </span>
33:   </li>
34:   <li style="margin-top:0.75pt; margin-left:31.71pt; padding-left:1.79pt; font-size:9pt">
35:     <span>
36:       Staff
37:     </span>
38:     <span>
39:       friendliness
40:     </span>
41:   </li>
42:   <li style="margin-top:0.7pt; margin-left:31.38pt; padding-left:2.12pt; font-size:9pt">
43:     <span>
44:       Cleanliness
45:     </span>
46:   </li>
47:   <li style="margin-top:0.7pt; margin-left:31.72pt; padding-left:1.78pt; font-size:9pt">
48:     <span>
49:       Atmosphere
50:     </span>
51:   </li>
52:   <li style="margin-top:0.75pt; margin-left:31.15pt; padding-left:2.35pt; font-size:9pt">
53:     <span>
54:       Value
55:     </span>
56:     <span>
57:       for
58:     </span>
59:     <span>
60:       money
61:     </span>
62:   </li>
63:   <li style="margin-top:0.7pt; margin-left:31.99pt; padding-left:1.51pt; font-size:9pt">
64:     <span>
65:       Other
66:     </span>
67:     <span>
68:       (please
69:     </span>
70:     <span>
71:       specify):
72:     </span>
73:     <span>
74:       [TEXT]
75:     </span>
76:   </li>
77: </ol>
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),
    Example(
        input=textwrap.dedent(
            """
1: <p style="margin:9.95pt 65.3pt 0pt 10.6pt; font-size:9pt" id="Q6">
2:   <span>
3:     [Q6] How likely are you to recommend our coffee shop to friends or family?
4:   </span>
5:   <span>
6:     0 (Not at all likely) to 10 (Extremely likely)
7:   </span>
8: </p>
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),
    Example(
        input=textwrap.dedent(
            """
1: <h1 style="margin-top:2.35pt; margin-left:29.75pt; margin-bottom:0pt; text-indent:-19.15pt; font-size:13.5pt" id="Q7">
2:   <span>
3:     <span style="color:#18186f">
4:       3.
5:     </span>
6:   </span>
7:   <span style="color:#18186f">
8:     Optional
9:   </span>
10:   <span style="color:#18186f">
11:     Open
12:   </span>
13:   <span style="color:#18186f">
14:     Feedback
15:   </span>
16: </h1>
17: <div>
18:   <p style="margin-top:4.35pt; margin-left:10.6pt; margin-bottom:0pt; font-size:9pt">
19:     <span>
20:       [Q7]
21:     </span>
22:     <span>
23:       Do
24:     </span>
25:     <span>
26:       you
27:     </span>
28:     <span>
29:       have
30:     </span>
31:     <span>
32:       any
33:     </span>
34:     <span>
35:       additional
36:     </span>
37:     <span>
38:       comments
39:     </span>
40:     <span>
41:       or
42:     </span>
43:     <span>
44:       suggestions
45:     </span>
46:     <span>
47:       for
48:     </span>
49:     <span>
50:       us?
51:     </span>
52:     <span>
53:       [LARGE
54:     </span>
55:     <span>
56:       TEXT
57:     </span>
58:     <span>
59:       BOX]
60:     </span>
61:   </p>
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),
    Example(
        input=textwrap.dedent(
            """
1:   <p style="margin-top:9.95pt; margin-left:10.6pt; margin-bottom:0pt; font-size:9pt" id="loyalty_score_calculation">
2:     <span style="font-size:7.5pt">
3:       [HIDDEN]
4:     </span>
5:     <span>
6:       loyalty_score
7:     </span>
8:     <span>
9:       =
10:     </span>
11:     <span>
12:       CALCULATE_LOYALTY_SCORE(Q1,
13:     </span>
14:     <span>
15:       Q6)
16:     </span>
17:   </p>
18:   <p style="margin-top:9.65pt; margin-left:10.6pt; margin-bottom:0pt; font-size:9pt">
19:     <span style="font-size:7.5pt">
20:       [HIDDEN]
21:     </span>
22:     <span>
23:       submission_time
24:     </span>
25:     <span>
26:       =
27:     </span>
28:     <span>
29:       GET_CURRENT_TIMESTAMP()
30:     </span>
31:   </p>
32:   <p style="margin-top:0.85pt; margin-bottom:0pt; font-size:9pt">
33:   </p>
34:   <p style="margin:0pt 65.3pt 0pt 28.55pt; text-indent:-18pt; font-size:7.5pt">
35:     <span>
36:       FUNCTION
37:     </span>
38:     <span>
39:       CALCULATE_LOYALTY_SCORE(visit_frequency,
40:     </span>
41:     <span>
42:       recommendation_score) frequency_score = SWITCH(visit_frequency)
43:     </span>
44:   </p>
45:   <p style="margin-top:0.05pt; margin-left:46.5pt; margin-bottom:0pt; font-size:7.5pt">
46:     <span>
47:       CASE
48:     </span>
49:     <span>
50:       1:
51:     </span>
52:     <span>
53:       RETURN
54:     </span>
55:     <span>
56:       5
57:     </span>
58:     <span>
59:       //
60:     </span>
61:     <span>
62:       Daily
63:     </span>
64:   </p>
65:   <p style="margin:1.85pt 185.95pt 0pt 46.5pt; font-size:7.5pt">
66:     <span>
67:       CASE
68:     </span>
69:     <span>
70:       2:
71:     </span>
72:     <span>
73:       RETURN
74:     </span>
75:     <span>
76:       4
77:     </span>
78:     <span>
79:       //
80:     </span>
81:     <span>
82:       Several
83:     </span>
84:     <span>
85:       times
86:     </span>
87:     <span>
88:       a
89:     </span>
90:     <span>
91:       week CASE 3: RETURN 3
92:     </span>
93:     <span>
94:       // Once a week
95:     </span>
96:   </p>
97:   <p style="margin:0pt 185.95pt 0pt 46.5pt; font-size:7.5pt">
98:     <span>
99:       CASE
100:     </span>
101:     <span>
102:       4:
103:     </span>
104:     <span>
105:       RETURN
106:     </span>
107:     <span>
108:       2
109:     </span>
110:     <span>
111:       //
112:     </span>
113:     <span>
114:       A
115:     </span>
116:     <span>
117:       few
118:     </span>
119:     <span>
120:       times
121:     </span>
122:     <span>
123:       a
124:     </span>
125:     <span>
126:       month CASE 5: RETURN 1
127:     </span>
128:     <span>
129:       // Less often
130:     </span>
131:   </p>
132:   <p style="margin:0pt 226.3pt 0pt 28.55pt; text-indent:17.95pt; font-size:7.5pt">
133:     <span>
134:       CASE
135:     </span>
136:     <span>
137:       6:
138:     </span>
139:     <span>
140:       RETURN
141:     </span>
142:     <span>
143:       0
144:     </span>
145:     <span>
146:       //
147:     </span>
148:     <span>
149:       First
150:     </span>
151:     <span>
152:       visit END SWITCH
153:     </span>
154:   </p>
155:   <p style="margin-top:1.9pt; margin-bottom:0pt; font-size:7.5pt">
156:   </p>
157:   <p style="margin:0pt 78.15pt 0pt 28.55pt; font-size:7.5pt">
158:     <span>
159:       loyalty_score
160:     </span>
161:     <span>
162:       =
163:     </span>
164:     <span>
165:       (frequency_score
166:     </span>
167:     <span>
168:       *
169:     </span>
170:     <span>
171:       2)
172:     </span>
173:     <span>
174:       +
175:     </span>
176:     <span>
177:       (recommendation_score
178:     </span>
179:     <span>
180:       /
181:     </span>
182:     <span>
183:       2) RETURN ROUND(loyalty_score, 1)
184:     </span>
185:   </p>
186:   <p style="margin-top:0pt; margin-left:10.6pt; margin-bottom:0pt; font-size:7.5pt">
187:     <span>
188:       END
189:     </span>
190:     <span>
191:       FUNCTION
192:     </span>
193:   </p>
            """
        ),
        output=ChunkPartExtractorResponseFormat(entities=[]),
    ),
]