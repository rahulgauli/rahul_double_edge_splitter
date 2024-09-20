# global blob_index_runner   
# global splitter_index_runner
# global splitterA 
# global splitterB 
# global blob 
# global final_questions

### Calling this the run rabbit algorithm


global final_questions 

final_questions = [ ]





def rahul_splitter_b(blob, endpoint_splitter, blob_index_runner, splitter_index_runner):
    try:
        value = ""
        
        while blob_index_runner < len(blob)-1:
            value = value + blob[blob_index_runner]
            lhs_letter = blob[blob_index_runner] 
            rhs_letter = endpoint_splitter[splitter_index_runner]
            if lhs_letter == rhs_letter:
                second_marker = lhs_letter
                while True:

                    blob_index_runner += 1
                    lhs_letter =blob[blob_index_runner]
                    splitter_index_runner+=1
                    rhs_letter = endpoint_splitter[splitter_index_runner]
                    second_marker += lhs_letter 

                    if second_marker == endpoint_splitter:
                        rahul_splitter_a(blob, splitterA, blob_index_runner )                        

    except Exception as e:
        print(e)
        raise 


def rahul_splitter_a(blob, splitterA, splitterB):
    try:
        output_value = ""

        assert len(splitterA)>0
        assert len(blob)>0

        global blob_index_runner 
        blob_index_runner = 0
         
        # output_value = output_value + blob[blob_index_runner]

        while blob_index_runner < len(blob)-1:
            
            global splitterA_index_runner
            splitterA_index_runner = 0

            lhs_letter = blob[blob_index_runner]
            rhs_letter = splitterA[splitterA_index_runner]
            

            if lhs_letter == rhs_letter:
                marker = lhs_letter
                while True:
                    
                    blob_index_runner += 1 
                    lhs_letter = blob[blob_index_runner]
                    splitterA_index_runner += 1
                    rhs_letter = splitterA[splitterA_index_runner]
                    marker += lhs_letter
                    
                    if lhs_letter != rhs_letter:
                        output_value += marker
                        break
                    
                    if marker == splitterA:

                        rahul_splitter_b(blob, splitterB, blob_index_runner+1)

            blob_index_runner += 1  
            output_value = output_value + blob[blob_index_runner]



                    

        # length_of_marker = len(splitterA)
        # questions = []
        # pointer = 0
        # while length_of_marker<len(blob):
        #     marker = ""
        #     for i in range(pointer, length_of_marker):
        #         marker = marker + blob[i]

        #     pointer = pointer+9
        #     length_of_marker = length_of_marker + 9
        #     print(pointer, length_of_marker)
        #     if marker == splitterA:
        #         print(marker)
        #         end_marker = ""
        #         while end_marker != splitterB:
        #             for i in range(pointer, length_of_marker):
        #                 end_marker = end_marker + blob[pointer]
        #             if end_marker == splitterB:
        #                 print(end_marker)
        #             else:
                        # print(end_marker)
        # print(length_of_marker)
        # while pointer<len(blob):
        #     temp_marker = ""
        #     for a_letter_ in (0,length_of_marker):
        #         new_letter = blob[a_letter_]
        #         temp_marker = temp_marker + new_letter
        #     print(temp_marker)
        # return questions
    except Exception as e:
        print(e)
        raise 


splitterA = "Question:"
splitterB = "Solution:"
with open("questions.txt", "r+") as f:
    blob = f.read()
    rahul_splitter_a(blob, splitterA, splitterB)