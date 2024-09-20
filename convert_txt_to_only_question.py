# global blob_index_runner   
# global splitter_index_runner
# global splitterA 
# global splitterB 
# global blob 
# global final_questions

### Calling this the run rabbit algorithm
### it keeps on running from one place to the other to collectively and recursively get question only 


global first_values  
first_values = [ ]

global blob_index_runner 
blob_index_runner = 0

global second_values
second_values = [ ]

global first_second_mapped_json 
first_second_mapped_json = { }


def rahul_splitter_b(blob, endpoint_splitter, blob_index_runner):
    try:
        value = ""
        # print(endpoint_splitter, blob_index_runner)

        while blob_index_runner < len(blob)-1:
            
            global splitterB_index_runner 
            splitterB_index_runner = 0 

            value = value + blob[blob_index_runner]
            
            lhs_letter = blob[blob_index_runner] 
            rhs_letter = endpoint_splitter[splitterB_index_runner]
            
            if lhs_letter == rhs_letter:
                second_marker = lhs_letter

                while True:

                    blob_index_runner += 1
                    lhs_letter =blob[blob_index_runner]
                    splitterB_index_runner+=1
                    rhs_letter = endpoint_splitter[splitterB_index_runner]
                    second_marker += lhs_letter 
                    
                    if lhs_letter != rhs_letter:
                        value += second_marker
                        break
                    
                    if second_marker == endpoint_splitter:
                        first_values.append(value)
                        response = rahul_splitter_a(blob, splitterA, splitterB , blob_index_runner=blob_index_runner)      
                        if response is None:
                            return
            blob_index_runner += 1  
            value = value + blob[blob_index_runner]
        first_values.append(value)
        return
    except Exception as e:
        print(e)
        raise 


def rahul_splitter_a(blob, splitterA, splitterB, blob_index_runner=blob_index_runner):
    try:
        # print(f"we are in the First slice {splitterA}")

        output_value = ""

        assert len(splitterA)>0
        assert len(blob)>0
         
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
                        # print(splitterB, blob_index_runner+1)
                        second_values.append(output_value)
                        response =rahul_splitter_b(blob, splitterB, blob_index_runner+1)
                        if response is None:
                            return
            blob_index_runner += 1  
            output_value = output_value + blob[blob_index_runner]
        second_values.append(output_value)
        return
    except Exception as e:
        print(e)
        raise 


splitterA = "Question:"
splitterB = "Solution:"
with open("questions.txt", "r+") as f:
    blob = f.read()
    rahul_splitter_a(blob, splitterA, splitterB)
    for a_equestion_ in first_values:
        print(a_equestion_)

    for a_solution in second_values:
        print(a_solution)
    print(len(second_values))
    print(len(first_values))