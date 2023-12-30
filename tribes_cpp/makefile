CC := g++
CFLAGS :=

SRC_DIR := src
OBJ_DIR := obj
BIN_DIR := build

SRC_FILES := $(shell find ./ -name "*.cpp")
OBJ_FILES := $(subst $(SRC_DIR),$(OBJ_DIR),$(subst .cpp,.o,$(SRC_FILES)))
SRC_DIRECTORIES = $(dir $(SRC_FILES))
OBJ_DIRECTORIES = $(subst $(SRC_DIR),$(OBJ_DIR),$(SRC_DIRECTORIES))

OBJ_FILES_WITHOUT_TEST = $(filter-out ./$(OBJ_DIR)/test.o,$(OBJ_FILES))
OBJ_FILES_WITHOUT_MAIN = $(filter-out ./$(OBJ_DIR)/main.o,$(OBJ_FILES))

show_files : 
	@echo $(SRC_FILES)

main : clean_obj clean_bin make_dirs $(OBJ_FILES_WITHOUT_TEST)
	$(CC) $(CFLAGS) $(OBJ_FILES_WITHOUT_TEST) -o $(BIN_DIR)/main

test : clean_obj clean_bin make_dirs $(OBJ_FILES_WITHOUT_MAIN)
	$(CC) $(CFLAGS) $(OBJ_FILES_WITHOUT_MAIN) -o $(BIN_DIR)/test

clean_obj :
	$(shell rm -rf $(OBJ_DIR)/*)

clean_bin :
	$(shell rm -rf $(BIN_DIR)/*)

make_dirs : 
	@$(foreach dir,$(OBJ_DIRECTORIES),mkdir -p $(dir);)

$(OBJ_DIR)/%.o : $(SRC_DIR)/%.cpp
	$(CC) $(CFLAGS) -c $< -o $@
	
