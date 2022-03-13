'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require("vscode");
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed

//  ###### 自定的 pastData ############################################################
const fs = require('fs')
function pasteData(myData){
    let editor = vscode.window.activeTextEditor, 
    document = editor.document, 
    selections = editor.selections;        

    editor.edit(function (editBuilder) {
        selections.forEach(function (selection) {
            if (!selection.isSingleLine) {
                return;
            }
            let range = new vscode.Range(selection.start, selection.end);
            editBuilder.replace( selection,  myData  );
        });
    });    
}
//  ###### 自定的 pastData ############################################################

function activate(context) {
    // Use the console to output diagnostic information (console.log) and errors (console.error)
    // This line of code will only be executed once when your extension is activated
    console.log('Congratulations, your extension "helloworld" is now active!');
    // The command has been defined in the package.json file
    // Now provide the implementation of the command with  registerCommand
    // The commandId parameter must match the command field in package.json
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        // The code you place here will be executed every time your command is executed
        // Display a message box to the user
        vscode.window.showInformationMessage('Hello World!');
    });
    context.subscriptions.push(disposable);

    //////// 這裡開始 //////////
    context.subscriptions.push(vscode.commands.registerCommand('extension.MYDATA000001', () => {
        var codeStr = `我的測試內容 ABC001`
        pasteData(codeStr)
    }));
    context.subscriptions.push(vscode.commands.registerCommand('extension.MYDATA000002', () => {
        var codeStr = `我的測試內容 ABC002`
        pasteData(codeStr)
    }));
    context.subscriptions.push(vscode.commands.registerCommand('extension.MYDATA000003', () => {
        var codeStr = `我的測試內容 ABC003`
        pasteData(codeStr)
    }));

    ///REPLACE HERE///

    ////////// END 這裡開始 //////////

}
exports.activate = activate;
// this method is called when your extension is deactivated
function deactivate() {
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map